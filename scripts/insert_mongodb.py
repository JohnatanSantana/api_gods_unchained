"""
  Insert data to MongoDB
"""

import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.databases.mongodb import mongodb_get_collection
from src.utils.config import DATA_PATH

def read_csv(path_dir: str) -> pd.DataFrame:
    return pd.read_csv(path_dir,sep=',')

def write_mongo(data: pd.DataFrame):
  try:
    collection = mongodb_get_collection
    collection.insert_many(data.to_dict('records'))
    print('data_id')
  except NameError:
    print(NameError)  

def run():  
  df = read_csv(DATA_PATH)
  print(df)
  write_mongo(df)

if __name__ == "__main__":
  run()