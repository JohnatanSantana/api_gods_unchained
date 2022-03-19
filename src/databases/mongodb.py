import pandas as pd
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import OperationFailure
from functools import lru_cache
from src.utils.config import MONGODB_CLIENT, MONGODB_DATABASE

@lru_cache
def mongodb_client() -> MongoClient:
    try:
        return MongoClient(MONGODB_CLIENT)
    except OperationFailure:
        raise OperationFailure("Could not connect to server")
        
def get_collection(collection_name: str):
    client = mongodb_client()
    db = client[MONGODB_DATABASE]
    collection = db[collection_name]
    return collection