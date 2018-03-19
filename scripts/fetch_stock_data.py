'''fetches stock data from api'''
import sys
import pandas as pd
import constants
import utils


def fetch(symbol, config):
    '''fetches stock data from api, return as a pandas dataframe'''

    # fetch stock data for a symbol
    param_list = [
        'function=' + config['function'],
        'symbol=' + symbol,
        'outputsize=' + config['outputsize'],
        'datatype=' + config['datatype'],
        'apikey=' + config['apikey']
    ]

    url = utils.url_builder(constants.BASEURL, param_list)

    json_data = utils.get_json_from_url(url)
    dataframe = pd.DataFrame(list(json_data.values())[1])
    # print(dataframe)
    return dataframe

if __name__ == '__main__':
    fetch(str(sys.argv[1]), sys.argv[2])
