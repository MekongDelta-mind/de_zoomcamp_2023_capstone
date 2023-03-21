# de_zoomcamp_2023_capstone
the repo for the DE zoomcamp 2023 which was submitted for evaluation


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
	- for postgres+pgadmin --> docker compose up
	- for ingesting the data --> docker build <image> and then docker run -it with commands
	- for metabase
		- docker pull metabase/metabase:latest
		- docker run -d -p 3000:3000 --name metabase metabase/metabase
		- setting up the potgres to create the dashboard

Tools used for 

* making the gif - [Chrome Capture - screenshot & gif tool](https://chrome.google.com/webstore/detail/chrome-capture-screenshot/ggaabchcecdbomdcnbahdfddfikjmphe?hl=en-GB)


The Dashboard

![image](https://user-images.githubusercontent.com/47595700/226678517-27d2d532-0d9e-447a-b937-0f5b304ee34b.png)

Trips count gif
---
![Trips Count - chrome-capture-2023-2-21](https://user-images.githubusercontent.com/47595700/226678663-80249e48-a0ef-4d1c-a2eb-4a9693a8ea9d.gif)

Avg Trip Duration by ride type
---
![Avg Trip dur by Ride Types chrome-capture-2023-2-21](https://user-images.githubusercontent.com/47595700/226678934-81f1a8b9-99f2-4d78-9bea-3ea74dbc056c.gif)

Avg Trip Duration by Customer Type
---
![Avg Trip dur by  Customer Type chrome-capture-2023-2-21](https://user-images.githubusercontent.com/47595700/226679066-74f0434e-e7d3-4069-bd21-a0ca782ea0d2.gif)

# git related common codes executed throughout

git status

git add .
git status

git commit -m "docker-compose: for posgres and pg admin;dockerfile: for ingesting the data; ingest_bike_data: .py file for ingesting data"

git branch -a
git pull origin main
git push origin main
