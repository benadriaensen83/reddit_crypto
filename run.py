import data_collect
import pandas as pd
from tabulate import tabulate
from datetime import datetime

run = data_collect.DataCollect()

data = run.data_from_api('bitcoin')

# adjust UNIX timestamp from API to readable datetime

for i in range(len(data)):
    data[i]['created_adj'] = datetime.fromtimestamp(data[i]['created_utc']).strftime('%Y-%m-%d %H:%M:%S')

data = pd.DataFrame(data)
print(tabulate(data, headers = 'keys', tablefmt= 'fancy_grid'))
pd.DataFrame.to_csv(data[:10], 'reddit_comments.csv')