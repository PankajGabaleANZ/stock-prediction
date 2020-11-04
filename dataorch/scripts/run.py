"""driver module"""
import sys
import getopt
import time
#import fetch_combined_data
#import preprocess
#import neural_network
#import evaluate_neural_network
from google.cloud import bigquery
import pandas
from google.cloud import storage
from datetime import datetime
import string
import re
# Imports the Google Cloud client library
from google.cloud import logging

def main(argv):
    '''driver method'''
    start = time.time()

    client = bigquery.Client(location="US")
    print("Client creating using default project: {}".format(client.project))
    client = bigquery.Client(location="US")
    blobs = storage_client.list_blobs('b1-sjs')

    dataset = bigquery.Dataset('radiant-poet-290704.'+data  set_id)
    dataset = client.create_dataset(dataset, timeout=30)

    StringformergeQuery = "select DATE, SAFE_CAST(Open as FLOAT64) as Open , SAFE_CAST(High as FLOAT64) as High,\
        SAFE_CAST(Low as FLOAT64) as Low, SAFE_CAST(Close as FLOAT64) as Close, SAFE_CAST(Adj_Close as FLOAT64) as Adj_Close, \
            SAFE_CAST(VOlume as INT64) as Volume, Symbol from  "



    # try:
        # opts, _ = getopt.getopt(argv, 'fpn', ['fetch', 'preprocess', 'neuralnetwork', 'evalnn'])
    # except getopt.GetoptError:
        # print('run.py')
        # sys.exit(2)
# 
# 
    # single_opt = [opt[0] for opt in opts]
# 
# 
    #run pipeline in order according to command line options
    # if '-f' in single_opt or '--fetch' in single_opt:
        # print('-----fetching new data-----')
        #fetch
        # fetch_combined_data.fetch(
            # 'input/symbols',
            # 'input/indicators',
            # 'output/raw'
        # )
    # if '-p' in single_opt or '--preprocess' in single_opt:
        # print('-----preprocessing data-----')
        #fetch
        # preprocess.preprocess_batch(
            # 'output/raw',
            # 'output/preprocessed',
            # 0.8
        # )
    # if '-n' in single_opt or '--neuralnetwork' in single_opt:
        # print('-----training Neural Network models-----')
        # neural_network.train_batch(
            # 'input/symbols',
            # 'output/preprocessed',
            # 'output/models'
        # )
# 
    # if '--evalnn' in single_opt:
        # print('-----Evaluating Neural Network models-----')
        # evaluate_neural_network.evaluate_batch(
            # 'input/symbols',
            # 'output/preprocessed/test'
        # )
# 
    # elapsed = time.time() - start
# 
    # print('time elapsed: ' + str(round(elapsed, 2)) + " seconds")
    # print('-----program finished-----')
# 
# 
# 
    # validate
    # validate_stock_data.validate(
        # context[env]['output_raw'],
        # context[env]['output_valid']
    # )


if __name__ == '__main__':
    main(sys.argv[1:])
