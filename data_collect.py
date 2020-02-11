import requests
import pandas as pd
from tabulate import tabulate
import datetime

class DataCollect:

    def data_from_api(self):

        url = "https://api.pushshift.io/reddit/comment/search"

        querystring = {"sort": "%27asc%27", "q": "%27bitcoin%27", "size": "34"}

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

        print(response.text)

        data = response.json()['data']

        print(len(data))
        exit()
        return data

