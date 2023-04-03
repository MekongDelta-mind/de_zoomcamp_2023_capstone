# de_zoomcamp_2023_capstone
For the Final Capstone projectwe are going to use the Citi Bike Sharing data toget some insights and explain them using the vizualization . All the tools explained in the course has been used to help with the process.

## Problem Description
### An Intro about the Dataset:
---
Citi Bike is the nation's largest bike share program, with 27,000 bikes and over 1,700 stations across Manhattan, Brooklyn, Queens, the Bronx, Jersey City and Hoboken. This dataset is about the Bike Sharing service Citi Bank in NY. 

The official site is [here](https://citibikenyc.com/how-it-works)

The Dataset site is [here](https://s3.amazonaws.com/tripdata/index.html)

Some important info about the dataset from the site:
* This data has been processed to remove 
	1. trips that are taken by staff as they service and inspect the system.
	1. trips that are taken to/from any of our “test” stations (which we were using more in June and July 2013). 
	1. any trips that were below 60 seconds in length (potentially false starts or users trying to re-dock a bike to ensure it's secure).

### Data Dictionary:
---
- Ride ID = unique id for all the rides
- Rideable type = Types of bikes available for the riders like classic bikes,  docked bikes and electric bike
- Started at and Ended at = time at which the rides are starting
- Start station name = Name of the starting station
- Start station ID = ID of the starting  station
- End station name = Name of the ending station
- End station ID = ID of the ending station
- Start latitude  & Start longitude = lat and long of the starting point
- End latitude & End Longitude = lat and long of the ending point
- Member or casual ride = representing whether a rider is a member ( who has a subscription ) or not a member ( casual rider who doesn’t have the a subscription )

### Description of files and folders:

- `ingest_bike_data.py` - contains the all the code used to transform the data and save in the required format
- `docker-compose.yml`- helps to build the docker image which would be used to create the container with required environment binding them into a common network.
- `Dockerfile` - used to copy the ingest file to the docker conatiner created int he above step with the required packages and running the python
- `[README.md](http://README.md)` - (the file you are reading) gives a brief intro about the project and conatins the instructions on how to reproduce the project.
- `dbt` = this is files related to dbt which helps in Analytics Engineering. This is currently not implemented. Facing issues with setting up the source and querying.

## Cloud

The project has been developed without using any cloud technologies. 

[//]: # (For EVERY week in the course write what are the technologies used instead of using the GCP,AWS or AZURE.This will be very easy for people who want to do the hand-ons without the GCP registeration)

## Data ingestion (choose either batch or stream)

The data would be monthly generated and from the business persepective it is fruitful to ingest the data monthly rather than weekly or daily.
Therefore we are using here the Batch processing way of ingesting the data. 
For the time being once the postgres and pgadmin is setup , we need to run the docker commands manually to ingest the data. Also there is no scheduling( monthly ) done yet. Both can be done using the Prefect parameterized flow and Prefect scheduling feature.


## Data warehouse

As weare not using GCP for the project, we are considering the Progres Database as our Warehouse, which contains the data which will be used to gain insights

## Transformations (dbt, spark, etc)

This involves analytics engineering to transform the data after the data has been ingested into the DWH. dbt will be used to the same. For the time being, there are no transformation done. [//]: # (FACING SOME CHALLENGES WITH CONFIGURING THE DBT ON LOCAL MACHINE.)

## Dashboard
We are using the Metabase as our Data Vizualization tool. The Postgres is used as the source of data for Metabase. As the whole project is done on local machine, so the Screenshots and gifs of the dashboard has been provided below.


<!-- You can build a dashboard with any of the tools shown in the course [Data Studio or Metabase] or any other BI tool of your choice. 
If you do use another tool, please specify and make sure that the dashboard is somehow accessible to your peers.
	* for this you can use your github actions to create the whole experience on the cloud and install metabase which will access the postgres
Your dashboard should contain at least two tiles, we suggest you include:

    [DONE]1 graph that shows the distribution of some categorical data
    1 graph that shows the distribution of the data across a temporal line
		adding a temporal related graph to show the variation over time.

[DONE]Make sure that your graph is clear to understand by adding references and title -->

## Reproducibility

















<!---

Sequence of commands executed:

sudo rm -rf bike_postgres_data

docker build -t bike_ingest:v001 .

docker compose up -d
docker compose down

the postgres should be activated and checked if the tables are created or not with all the config before running the docker

URL="https://s3.amazonaws.com/tripdata/202302-citibike-tripdata.csv.zip";
docker run -it \
	--network=de_zoomcamp_capstone_default \
	bike_ingest:v001 \
	--user=root \
	--password=root \
	--host=pgdatabase_capstone \
	--port=5432 \
	--db=bike_sharing \
	--table_name=bike_sharing_trips \
	--url=${URL}



METABASE + POSTGRES + PGADMIN + DATA INGESTED

POSTGRES + PGADMIN

cd Workspace/de_zoomcamp_capstone/
docker compose up -d

docker compose down

DATA INGESTED

URL="https://s3.amazonaws.com/tripdata/202302-citibike-tripdata.csv.zip";
docker run -it \
	--network=de_zoomcamp_capstone_default \
	bike_ingest:v001 \
	--user=root \
	--password=root \
	--host=pgdatabase_capstone \
	--port=5432 \
	--db=bike_sharing \
	--table_name=bike_sharing_trips \
	--url=${URL}
	
METABASE

docker run -d -p 3000:3000 --name metabase metabase/metabase


Reproducibility

clone the repo into another folder
- create the a new envi
	- with python 3.9.16
	- add the requirements.txt for the file
		- check with prefect version
			- add the prefect related libs
		- check with dbt --version	
			- add the dbt related libs
- docker desktop setup
- then the 
	- for postgres+pgadmin ==> docker compose up
	- for ingesting the data ==> docker build <image> and then docker run -it with commands
	- for metabase
		- docker pull metabase/metabase:latest
		- docker run -d -p 3000:3000 --name metabase metabase/metabase
		- setting up the potgres to create the dashboard
-->

Tools used for 

* making the gif - [Chrome Capture - screenshot & gif tool](https://chrome.google.com/webstore/detail/chrome-capture-screenshot/ggaabchcecdbomdcnbahdfddfikjmphe?hl=en-GB)


## The Dashboard

![image](https://user-images.githubusercontent.com/47595700/226678517-27d2d532-0d9e-447a-b937-0f5b304ee34b.png)

### Trips count gif
---
![Trips Count - chrome-capture-2023-2-21](https://user-images.githubusercontent.com/47595700/226678663-80249e48-a0ef-4d1c-a2eb-4a9693a8ea9d.gif)

### Avg Trip Duration by ride type
---
![Avg Trip dur by Ride Types chrome-capture-2023-2-21](https://user-images.githubusercontent.com/47595700/226678934-81f1a8b9-99f2-4d78-9bea-3ea74dbc056c.gif)

### Avg Trip Duration by Customer Type
---
![Avg Trip dur by  Customer Type chrome-capture-2023-2-21](https://user-images.githubusercontent.com/47595700/226679066-74f0434e-e7d3-4069-bd21-a0ca782ea0d2.gif)

<!---
# git related common codes executed throughout the project lifecycle

git status

git add .
git status

git commit -m "docker-compose: for posgres and pg admin;dockerfile: for ingesting the data; ingest_bike_data: .py file for ingesting data"

git branch -a
git pull origin main
git push origin main

-->
