import pandas as pd
from pymongo import MongoClient
# import urlib.parse

# username = urllib.parse.quote_plus('root')
# password = urllib.parse.quote_plus('passwd1234')

client = MongoClient('mongodb://root:passwd1234@127.0.0.1:27017/')

db = client['godcards']
collection = db['cards']

def read_csv(path_dir: str) -> pd.DataFrame:
    return pd.read_csv(path_dir,sep=',')

path = "data/challenge_test.csv"
df = read_csv(path)
# print(df)

def read_mongo(data):
  try:
    # data_id = collection.insert_one(data_dict).inserted_id
    mongo_data = collection.find_one(data)
    if mongo_data is None:
      raise ValueError("id do not exists in our database")
    mongo_data.pop('_id')
    return mongo_data
  except NameError:
    print(NameError)  
data_r = {"id": 100042}
df = read_mongo(data_r)
import pdb
pdb.set_trace()