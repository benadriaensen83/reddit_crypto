import data_collect
import pandas as pd
from tabulate import tabulate
from datetime import datetime
from time import time
import combine_data

# initialise classes
run = data_collect.DataCollect()

# collect data from API
data = run.data_from_api('bitcoin')

# adjust UNIX timestamp from API to readable datetime
for i in range(len(data)):
    data[i]['created_adj'] = datetime.fromtimestamp(data[i]['created_utc']).strftime('%Y-%m-%d %H:%M:%S')

# create dataframe from data and write to pickle

data = pd.DataFrame(data)

print(tabulate(data, headers = 'keys', tablefmt= 'fancy_grid'))
pd.DataFrame.to_pickle(data, 'csv_files/reddit_comments_' + str(time()) + '.pkl')

# combine existing pickle files with last data

combine_data.combine()
