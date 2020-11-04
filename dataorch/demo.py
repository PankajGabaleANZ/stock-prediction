from google.cloud import bigquery
import pandas
from google.cloud import storage
from datetime import datetime
import string
import re


client = bigquery.Client(location="US")
print("Client creating using default project: {}".format(client.project))
# client = bigquery.Client(location="US", project="your-project-id")4