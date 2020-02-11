import requests
import pandas as pd
from tabulate import tabulate

class DataCollect:

    def data_from_api(self):

        url = "https://api.pushshift.io/reddit/comment/search"

        querystring = {"sort":"%27asc%27","q":"%27bitcoin%27","size":"20"}

        headers = {
            'User-Agent': "PostmanRuntime/7.13.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "7b7818c5-f2bd-4962-950d-31c6ebc5ac94,661f03fd-9fb7-4734-a8b2-3b8ff3a1d19f",
            'Host': "api.pushshift.io",
            'cookie': "__cfduid=df6ffa9e102960abbcbe896ecfd332d071581425174",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()['data']

        return data

