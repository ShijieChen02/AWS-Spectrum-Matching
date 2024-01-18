CREATE EXTERNAL TABLE IF NOT EXISTS spectrum_distance_observatory_fact_df (
    spectrum_id string,
    distance double,
    observatory_id int
)
PARTITIONED BY (year INT, month INT, day INT)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://your-s3-bucket/your-json-data-directory/'; # where you put distance data

CREATE EXTERNAL TABLE IF NOT EXISTS observatory_spectrum_distance_app_df (
    observatory_id int
    ,avg_dis double
    ,min_dis double
    ,max_dis double
)
STORED AS parquet
LOCATION 's3://your-s3-bucket/target-table/'; # where you want to put the result


INSERT OVERWRITE TABLE observatory_spectrum_distance_app_df PARTITION (year=year(date_add(current_utc_timestamp, -1)) , month=month(date_add(current_utc_timestam, -1)), day=day(date_add(current_utc_timestamp, -1))) # replace 
select
    observatory_id
    ,avg(distance) as avg_dis
    ,min(distance) as min_dis
    ,max(distance) as max_dis
from spectrum_distance_observatory_fact_df
where year = year(date_add(current_utc_timestamp, -1)) and month = month(date_add(current_utc_timestam, -1)) and day = day(date_add(current_utc_timestamp, -1)) 
group by observatory_id
