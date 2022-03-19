"""
  Insert data to MongoDB
"""
import logging
import pandas as pd
from src.utils.config import DATA_PATH, MONGODB_COLLECTION
from src.databases.mongodb_dml import write_many, get_collection


def read_csv(path_dir: str) -> pd.DataFrame:
    return pd.read_csv(path_dir, sep=',')


def run():
    df_pd = read_csv(DATA_PATH)
    data_dict = df_pd.to_dict('records')
    write_many(MONGODB_COLLECTION, data_dict)


if __name__ == "__main__":

    if get_collection(MONGODB_COLLECTION).find_one() is None:
        logging.info("Inserindo dados no MongoDB")
        run()
    else:
        logging.info("Dados Já existem no MongoDB")
