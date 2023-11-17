import os
from google.cloud import bigquery

# Set ENV variable for google authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './service_account.json'

# Create a client object
client = bigquery.Client()

# SQL query to execute
query = """
    SELECT * FROM `bigquery-public-data.catalonian_mobile_coverage_eu.mobile_data_2015_2017` LIMIT 10
"""
query_job = client.query(query)  # Make an API request

print(type(query_job))

# Print the results
for row in query_job:
    # row values can be accessed by field name or index
    print(row)
    print("\n")
