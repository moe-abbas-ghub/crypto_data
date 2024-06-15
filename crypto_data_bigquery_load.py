#!/usr/bin/env python3
import yfinance as yf
import datetime as dt
import os
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd

# Define the start and end dates
Start = '1900-01-01'  # A very early date to get all historical data
End = dt.datetime.now().strftime('%Y-%m-%d')  # Current date

CryptoList = ['BTC-USD', 'BTC-EUR', 'ETH-USD', 'ETH-EUR']

# Download data
Crypto_Df = yf.download(CryptoList, start=Start, end=End)['Adj Close']
Crypto_Df = Crypto_Df.reset_index()

# Set up BigQuery client
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your-service-account-file.json'
)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Define your BigQuery dataset and table name
dataset_id = 'dataset_id'
table_id = 'table_id'
full_table_id = f'{client.project}.{dataset_id}.{table_id}'

# Configure the load job
job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)

# Load DataFrame to BigQuery table
job = client.load_table_from_dataframe(Crypto_Df, full_table_id, job_config=job_config)

# Wait for the load job to complete
job.result()

print(f"Loaded {job.output_rows} rows into {full_table_id}.")
