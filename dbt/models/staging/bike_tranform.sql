{{ config(materialized='view') }}

-- even the database chnages , the model will search for name 
-- staging in the source and for the table name bike_sharing_trips
select * from 
{{ source('bike_tranform', 'bike_sharing_trips') }} 
limit 100 