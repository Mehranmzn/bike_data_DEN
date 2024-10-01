import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import io
import duckdb
from zipfile import ZipFile


defual_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,

}

dag = DAG(
    'city_bike_ingestion_duckdb',
    defual_args=defual_args,
    description = 'A dag to ingest Citi bike data from S3 bucket and load it inot Duck db',
    shedule_interval = 'monthly',
    cathup = False  
)





