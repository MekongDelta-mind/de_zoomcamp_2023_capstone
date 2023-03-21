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


# git related common codes executed throughout

git status

git add .
git status

git commit -m "docker-compose: for posgres and pg admin;dockerfile: for ingesting the data; ingest_bike_data: .py file for ingesting data"

git branch -a
git pull origin main
git push origin main