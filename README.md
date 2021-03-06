# Comparing static and dynamic effects of earthquakes on the ground surfaces

Damages produced by earthquakes are caused by permanent surface deformation due to fault offset, as well as dynamic shaking due to the pass of seismic waves. The investigation of the relationship between such physical processes may provide a better understanding of earthquake hazard. To this aim, complete and homogeneous catalogues are necessary. Regarding dynamic changes, data are constantly acquired by seismic stations installed on the ground surface, and the so called “ShakeMaps” are generated after a seismic event by relying on their measurements. Instead, co-seismic deformation can be measured with different geodetic techniques. For example, surface deformation maps can be generated via Differential SAR interferometry (DInSAR). The DInSAR analyses performed so far have consolidated this technique as extremely important to map and characterize co-seismic deformation. However, analyses are generally performed for specific cases, by relying on different software solutions, as well as different processing parameters. Thus, results are often not complete and/or extremely heterogeneous.

The focus of the exercise would be to find a convenient way of exploitation of the results. The idea is to develop a procedure to produce geocoded maps combining automatically the important results to have a convenient visualisation that would help for the results interpretation.

Example: Overlay of interferometric phase + shake map + EQ epicenter for the Earthquake occurred on Nov 12, 2017 Mw 7.3 on the Iran-Iraq border region. This visualisation has been produced "offline", by downloading the interferogram results from the infohub and the ShakeMap + epicenter files as .kml from the USGS webpage

![image info](.image2020-7-27_15-50-55.png)

## Information about the events:

The events below can be used duing this exercise:

* https://earthquake.usgs.gov/earthquakes/eventpage/us7000bctq/executive
* https://earthquake.usgs.gov/earthquakes/eventpage/us7000bcty/executive
* https://earthquake.usgs.gov/earthquakes/eventpage/us7000bfjx/executive
* https://earthquake.usgs.gov/earthquakes/eventpage/us7000bg4v/executive

See the notebook us7000bctq.ipynb or us7000birm.ipynb to get started

## Run the notebook on Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ec-better/hackathon-2020-ETHZ/master?urlpath=lab)

Binder runs the experiments for free with computing resources provided by Google Cloud, OVH, GESIS Notebooks and the Turing Institute.
The notebook must target a computing environment with 2 GB of RAM

After some inactivity, the docker container is culled. 

### Run the notebook locally using docker

Clone this repository with:

```bash
git clone https://github.com/ec-better/hackathon-2020-ethz.git
```

Go to the directory containing the cloned repository:

```bash
cd hackathon-2020-ethz
```

Use docker compose to build the docker image:

```bash
docker-compose build
```

This step can take a few minutes...

Finally run the docker with:

```
docker-compose up
```

Open a browser window at the address http://0.0.0.0:9005 or http://127.0.0.1:9005 and run the notebook

## Additional guidelines

There are a few knowledge base entries here https://knowledge.terradue.com/display/ELLIP/Ellip+Notebooks+user+guides showing how to common tasks with a Notebook 
