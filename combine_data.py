import pandas as pd
import glob
import os

def combine():

    files = glob.glob('csv_files/*.pkl')
    data = pd.concat([pd.read_pickle(fp) for fp in files], ignore_index=True, sort= True)
    for fp in files:
        os.remove(fp)
    pd.DataFrame.to_pickle(data, 'csv_files/consolidated.pkl')
    pd.DataFrame.to_csv(data, 'csv_files/consolidated.csv')
    print(data)


