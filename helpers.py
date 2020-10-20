
from urllib.parse import urlparse
import gdal 
import numpy as np

def hello():
    
    print('Hello World!')


def get_vsi_url(enclosure, username=None, api_key=None):
    
    
    parsed_url = urlparse(enclosure)

    if username is not None:
        
        url = '/vsicurl/{}://{}:{}@{}/api{}'.format(list(parsed_url)[0],
                                                username, 
                                                api_key, 
                                                list(parsed_url)[1],
                                                list(parsed_url)[2])
    
    else:
        
        url = '/vsicurl/{}://{}/api{}'.format(list(parsed_url)[0],
                                              list(parsed_url)[1],
                                              list(parsed_url)[2])
    
    return url 


def vsi_download(enclosure, bbox=None, username=None, api_key=None):
    
    vsi_url = get_vsi_url(enclosure, username, api_key)
    
    # load VSI URL in memory
    output = '/vsimem/subset.tif'
    
    ds = gdal.Open(vsi_url)
    
    if bbox is not None:
        ulx, uly, lrx, lry = bbox[0], bbox[3], bbox[2], bbox[1] 
    
        ds = gdal.Translate(destName=output, 
                            srcDS=ds, 
                            projWin = [ulx, uly, lrx, lry], 
                            projWinSRS = 'EPSG:4326',
                            outputType=gdal.GDT_Float32)
        
    else:
        
        ds = gdal.Translate(destName=output, 
                            srcDS=ds, 
                            outputType=gdal.GDT_Float32)
    ds = None
    
    # create a numpy array
    ds = gdal.Open(output)
    
    layers = []

    for i in range(1, ds.RasterCount+1):
        layers.append(ds.GetRasterBand(i).ReadAsArray())

    return np.dstack(layers)