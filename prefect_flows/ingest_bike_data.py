#!/usr/bin/env python
# coding: utf-8
import os
import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine
import zipfile
from prefect import flow, task, tasks
from datetime import timedelta


@task(
          name="Extract the data",
          log_prints=True, 
          retries = 3, 
          cache_key_fn=tasks.task_input_hash, # caching hte data to not download every single time
          cache_expiration=timedelta(days=1)
          )
def extract_data(url: str):
    # the backup files are gzipped, and it's important to keep the correct extension
    # for pandas to be able to open the file    
    csv_name = '202302-citibike-tripdata.csv'
    os.system(f"wget {url} ")

    zip_filename = '202302-citibike-tripdata.csv.zip'
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall()
        print(f'{zip_filename} is extracted successfully')

    raw_data = pd.read_csv(csv_name, iterator=True, chunksize=100000) # the chunk size to be changed

    df = next(raw_data)
    
    print(f'shape of df {df.shape}')
    
    # Convert starttime and stoptime to datetime format
    df['started_at'] = pd.to_datetime(df['started_at'])
    df['ended_at'] = pd.to_datetime(df['ended_at'])

    return df

@task(    
          name="Transform data",
          log_prints=True, 
         )
def transform_data(df):
    print(f"null values count for columns before dropping: \n {df.isna().sum()}")
    df.dropna(axis=0, inplace=True)
    print(f"null values count for columns after dropping \n {df.isna().sum()}")

    df['tripduration_msecs'] = df['ended_at'] - df['started_at']
    df['tripduration_mins'] = df['tripduration_msecs'] / 60
    print(f'tripduration_mins and tripduration_msecs calculated and added to the df \n')

    return df

@task(    
          name="Loading the data",
          log_prints=True, 
         )
def load_data(user, password, host, port, db, table_name, data_df):

        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

        # the step to create the engine from the url is abstracted by using the connector. Rest of the code remaings the same.
        data_df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace') # this it adding the columns to db
        data_df.to_sql(name=table_name, con=engine, if_exists='append')

@flow(
          name="Subflow for Logging", 
         )
def log_subflow(db: str, table_name: str):
    print(f"Logging Subflow for db: {db} and table:{table_name}")


@flow(
          name="Bike Trips Data Ingestion Flow", 
          description= "The Prefect Flow to ingest the data into the Postgres database"
          )
def main_flow():
		# first run the prefect flow without sending the cred as paramters  
		# then you can send a parameterized flow
    user = "root" # the username  is changed from original file
    password = "root" # the password is changed from original file
    host = "localhost"
    port = "5432"
    db = "bike_sharing" # db name
    table_name = "bike_sharing_trips" # table name
    csv_url = "https://s3.amazonaws.com/tripdata/202302-citibike-tripdata.csv.zip"

    # user = args.user
    # password = args.password
    # host = args.host 
    # port = args.port 
    # db = args.db
    # table_name = args.table_name
    # csv_url = args.url
		
		# flows conatins tasks which allows to have dependencies before and after 
		# the task is completed so that a task waits till the pther task completes

    log_subflow(db, table_name)
    raw_data = extract_data(csv_url)
    data = transform_data(raw_data)
    # send all the creds for the postgres
    load_data(user, password, host, port, db, table_name, data)
    # a flow conatins tasks, as the ingest data method is added to the main function so ingest data would be a task
    #ingest_data(user, password, host, port, db, table_name, csv_url)

if __name__ == '__main__':
    # while adding the prefect code this is to be removed as we will be using the prefect connector directly
    main_flow()