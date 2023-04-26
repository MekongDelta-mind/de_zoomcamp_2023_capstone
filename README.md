- [de_zoomcamp_2023_capstone](#de-zoomcamp-2023-capstone)
  * [Problem Description](#problem-description)
    + [An Intro about the Dataset:](#an-intro-about-the-dataset)
    + [Data Dictionary:](#data-dictionary)
    + [Description of files and folders:](#description-of-files-and-folders)
  * [Cloud](#cloud)
  * [Data ingestion (choose either batch or stream)](#data-ingestion-choose-either-batch-or-stream)
  * [Data warehouse](#data-warehouse)
  * [Transformations (dbt, spark, etc)](#transformations-dbt-spark-etc)- NOT IMPLETMENTED YET
  * [Dashboard](#dashboard)
  * [Reproducibility](#reproducibility)
  * [Tools used for](#tools-used-for) 
  * [The Dashboard](#the-dashboard)
    + [Trips count gif](#trips-count-gif)
    + [Avg Trip Duration by ride type](#avg-trip-duration-by-ride-type)
    + [Avg Trip Duration by Customer Type](#avg-trip-duration-by-customer-type)
  
  * [Future Improvements](#future-improvements)
- [Last but not the Least](#last-but-not-the-least)
<!-- - [git related common codes executed throughout the project lifecycle](#git-related-common-codes-executed-throughout-the-project-lifecycle) -->


# de_zoomcamp_2023_capstone
For the Final Capstone project we are going to use the Citi Bike Sharing data toget some insights and explain them using the vizualization . All the tools explained in the course has been used to help with the process.

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

The Question we are trying to answer are :
1. What are the total number of trips taken by both types(memeber and casual) of customers.
1. What is the avg trip duration for each types of bike ?
1. What is the avg trip duration for each types of members ?

### Data Dictionary:
---
- `Ride ID` = unique id for all the rides
- `Rideable type` = Types of bikes available for the riders like classic bikes,  docked bikes and electric bike
- `Started at` and `Ended at` = time at which the rides are starting
- `Start station name` = Name of the starting station
- `Start station ID` = ID of the starting  station
- `End station name` = Name of the ending station
- `End station ID` = ID of the ending station
- `Start latitude`  & `Start longitude` = lat and long of the starting point
- `End latitude` & `End Longitude` = lat and long of the ending point
- `Member` or `casual ride` = representing whether a rider is a member ( who has a subscription ) or not a member ( casual rider who doesn’t have the a subscription )

### Description of files and folders:

- `ingest_bike_data.py` - contains the all the code used to transform the data and save in the required format
- `docker-compose.yml`- helps to build the docker image which would be used to create the container with Postgres and Pgadmin image together, binding them into a common network.
- `Dockerfile` - used to copy the ingest file to the docker conatiner created int he above step with the required packages and running the python
- `README.md` - (the file you are reading) gives a brief intro about the project and conatins the instructions on how to reproduce the project.
- `prefect_flows` - the folder containing the prefect flows to execute the pipeline in the fomr of flow.
- `dbt` = this is files related to dbt which helps in Analytics Engineering. This is currently not implemented. Facing issues with setting up the source and querying.

## Cloud

The project has been developed without using any cloud technologies. The whole project is done loaclly and the stpes to recreate the project is mentioned in the [Reproducibility](#reproducibility) section.

[//]: # (For EVERY week in the course write what are the technologies used instead of using the GCP,AWS or AZURE.This will be very easy for people who want to do the hand-ons without the GCP registeration)

## Data ingestion (choose either batch or stream)

The data would be monthly generated and from the business persepective it is fruitful to ingest the data monthly rather than weekly or daily.
Therefore we are using here the Batch processing way of ingesting the data. 
For the time being once the postgres and pgadmin is setup , we need to run the docker commands manually to ingest the data. Prefect is being used to create the flow to ingest the data by running it locally.


## Data warehouse

As we are not using GCP for the project, we are considering the Progres Database as our Warehouse, which contains the data which will be used to gain insights using the Metabase tool.

<!--## Transformations (dbt, spark, etc)-->

<!-- This involves analytics engineering to transform the data after the data has been ingested into the DWH. dbt will be used to the same. For the time being, there are no transformation done. 
[//]: # ( FACING SOME CHALLENGES WITH CONFIGURING THE DBT ON LOCAL MACHINE.) -->

## Dashboard
We are using the Metabase as our Data Vizualization tool. The Postgres is used as the source of data for Metabase. As the whole project is done on local machine, so the Screenshots and gifs of the dashboard has been provided below in the [The Dashboard](#the-dashboard) section.


<!-- You can build a dashboard with any of the tools shown in the course [Data Studio or Metabase] or any other BI tool of your choice. 
If you do use another tool, please specify and make sure that the dashboard is somehow accessible to your peers.
	* for this you can use your github actions to create the whole experience on the cloud and install metabase which will access the postgres
Your dashboard should contain at least two tiles, we suggest you include:

    [DONE]1 graph that shows the distribution of some categorical data
    1 graph that shows the distribution of the data across a temporal line
		adding a temporal related graph to show the variation over time.

[DONE]Make sure that your graph is clear to understand by adding references and title -->

## Reproducibility

1. Create a new folder for cloning the repo into your folder
2. Clone the  project by using the command `git clone <url-to-the-repo> .`  . If the  repos contents are copied into you new folder, then this step is successful.
3. You can skip this step if you running the project for the first time OR Just for sanity check try to run the command `sudo rm -rf bike_postgres_data` to remove the volume data from your local machine if you have ran the project before. 
4. Check if you already have Dokcer installed in your system by running the command `docker --version`. if not use the link [Docker desktop setup](https://docs.docker.com/desktop/) to install Docker Desktop according to your OS.
<!-- 5. After checking if the Docker file is present , run the command `docker build -t bike_ingest:v001 .` . This step will create the image from the Dockerfile. You can check  in teh Docker dsktop if an image with name “bike_ingest” is created or not . -->
5. Next is to run the (Postgres + Pgadmin ) for accessing  the database for quick queries on the database byusing the command `docker compose up -d` .
6. Access the [pgadmin url](http://localhost:8080) , to check if the pgadmin is working properly or not. Login with the creds [ usernam- `admin@admin.com` and password - `root` ].
    1. once you are logged in into postgres through pgadmin, try to create server 
        1. with name of the server of your choice 
        1. hostname = `name of the postgres db you created while running the docker compose up -d` 
        1. username = `root`
        1. password = `root`
        1. Save the config. if the config info are correct then you would have a server with the server of our choice without any error.
7. NOTE: By this stage The postgres should be activated which could be accessed by pgadmin GUI with all the required config before running the below docker command to ingest the data .
<!-- 8. Run the below command to ingest the data from the given url, run the image with the reuired network name to ingest the data into the database named as `bike_sharing` . 
    
    ```bash
    URL="[https://s3.amazonaws.com/tripdata/202302-citibike-tripdata.csv.zip](https://s3.amazonaws.com/tripdata/202302-citibike-tripdata.csv.zip)";
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
    ``` -->
8. As we are using Prefect for workflow orchestration, the way we are trying to ingest the data into the DB is bit different as follow:
  1. First create an virtual env with Python version = 3.9 (not tested with Python v=3.9+).
  1. Using the requirements.txt in the prefect folder, install the prefect dependencies into the environment. Check the prefect is installed properly by executing the command `prefect version` in CLI.
  1. Run the Prefect UI by executing the command `prefect orion start`.

      ```bash
      (de_zoomcamp_2023_capstone) prabin_nayak@DESKTOP-IUPLGMD:~$ prefect orion start

        ___ ___ ___ ___ ___ ___ _____    ___  ___ ___ ___  _  _
        | _ \ _ \ __| __| __/ __|_   _|  / _ \| _ \_ _/ _ \| \| |
        |  _/   / _|| _|| _| (__  | |   | (_) |   /| | (_) | .` |
        |_| |_|_\___|_| |___\___| |_|    \___/|_|_\___\___/|_|\_|

        Configure Prefect to communicate with the server with:

            prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

        View the API reference documentation at http://127.0.0.1:4200/docs

        Check out the dashboard at http://127.0.0.1:4200
      ```
      Check out the dashboard at http://127.0.0.1:4200 to check if you can access the Prefect Dashboard.

  1. Now we have to deploy our prefect flow to be able to execute the flow from the UI. 
      1. Make sure you are in the folder `prefect_flows` or else run `cd ./prefect_flows`. 
      1. Run the command `prefect deployment build ./ingest_bike_data.py:main_flow -n "Capstone Project Flow"` which will create a `main_flow-deployment.yaml` in the path `./prefect_flows`. This will help us to deploy the prefect flow into the server(the local server we have have been running through orion)
      1. Once the file is created then run the command `prefect deployment apply main_flow-deployment.yaml` to upload the deployment so that you cna see that in the UI.
      1. Now, though you can see the flow , even if you run it, it won't run. It is because ther is no agent to pick up the flow. So you have to select the `Work Queues` tab from the left side panel. And if you select the `default` queue you would see that the Flow is scheduled but there is no agent.
      1. To start an agent, you have to run the command `prefect agent start --work-queue "default"`. And then it will start the run.
    
9. How the Data Vizualizations was created :
    1. installing METABASE
        1. Pull the Metabase image from the DOckerHub by using the command `docker pull metabase/metabase:latest` .
        2. Run the metabase docker with teh command `docker run -d -p 3000:3000 --name metabase metabase/metabase`
        3. Access the url `localhost:3000/` to access the Metabase server running on your local instance.
        4. Check the below gif and screenshots for the dashboard created .
10. To stop the command Postgres + PGadmin running use the command `docker compose down` .


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

## Tools used for 

* Scripting the Data Ingest file - `Python`
* For Containerization - `Docker`
* For Datawarehouse - `Postgres`
* For Data Vizualization - `Metabase`
* Making the gif - [Chrome Capture - screenshot & gif tool](https://chrome.google.com/webstore/detail/chrome-capture-screenshot/ggaabchcecdbomdcnbahdfddfikjmphe?hl=en-GB)


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
# Future Improvements

1. Currently the transformations are being done in the python script itself. Adding the dbt transformation to create FACTS and DIMENSIONS table dynamically.
1. Adding the docker capabilities into the Prefect flow so that we can conatinerize the whole flow which can be setup in any host machine with a single command.
1. Adding the distributed processing using Spark.
1. Adding Stream processing based on feasibility and scope of the project.

# Last but not the Least...

Thanks to Datatalks club for creating this [Data Engineering course](https://github.com/DataTalksClub/data-engineering-zoomcamp) to help anyone and everyone to learn Data Engineering at ZERO COST. Other offerings by the Club are [ML Zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) and [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp). Do check them out !! 
