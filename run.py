import data_collect
import pandas as pd
from tabulate import tabulate


run = data_collect.DataCollect()
data = run.data_from_api()
print(len(data))
data = pd.DataFrame(data)
print(tabulate(data, headers = 'keys', tablefmt= 'fancy_grid'))
pd.DataFrame.to_csv(data, 'reddit_comments.csv')