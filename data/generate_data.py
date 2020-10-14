import numpy as np
import pandas as pd
from datetime import datetime as dt, timedelta
import sys

N_DATASETS = 3
args = sys.argv[1:]

if __name__ == "__main__":

    if len(args) == 1:
        N_DATASETS = int(args[0])

    for i in range(1,N_DATASETS+1):
        start_date = dt.now()
        days = int(np.random.randint(low=20,high=100,size=1)[0])
        end_date = start_date + timedelta(days=days)
        index = pd.date_range(start_date,end_date)
        values = np.random.randint(low=0,high=1000,size=days)
        df = pd.DataFrame(zip(index,values),columns=['timestamp','value'])
        df.to_csv(f'random_data_{i}.csv',index=False)