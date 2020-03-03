import requests
import pandas as pd
from tabulate import tabulate
import datetime
import sys

class DataCollect:

    def data_from_api(self, query, size):

        url = "https://api.pushshift.io/reddit/comment/search"

        querystring = {"sort": "desc", "q": query, "size": size}

        headers = {
            'User-Agent': "PostmanRuntime/7.13.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "d5979873-a5b6-4e5f-b40f-32458e7082c9,4fcaadea-15a7-49d8-8b05-891336fa493b",
            'Host': "api.pushshift.io",
            'cookie': "__cfduid=df6ffa9e102960abbcbe896ecfd332d071581425174",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()['data']

        print('total bytesize is {}'.format(str(sys.getsizeof(response.text))))
        print('total number of results is {}'.format(len(data)))

        return data

