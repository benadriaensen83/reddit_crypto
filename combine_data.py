import pandas as pd
import glob
import os
from tabulate import tabulate

def combine():

    files = glob.glob('csv_files/*.pkl')
    data = pd.concat([pd.read_pickle(fp) for fp in files], ignore_index=True, sort= True)
    for fp in files:
        os.remove(fp)

    data = data.drop_duplicates(subset=['permalink'])
    print(tabulate(data, headers='keys', tablefmt='fancy_grid'))

    # save as pickle for futuer appending and as csv for handing over to another app (e.g. Power BI)

    pd.DataFrame.to_pickle(data, 'csv_files/consolidated.pkl')
    pd.DataFrame.to_csv(data, 'csv_files/consolidated.csv')

