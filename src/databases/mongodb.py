from functools import lru_cache
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from src.utils.config import MONGODB_CLIENT, MONGODB_DATABASE


@lru_cache
def mongodb_client() -> MongoClient:
    """
        Create MongoDB Connection
    """
    try:
        return MongoClient(MONGODB_CLIENT)
    except OperationFailure:
        raise OperationFailure("Could not connect to server")


def get_collection(collection_name: str):
    """
        Get Collection from MongoDB
        args:
            collection_name str
    """
    client = mongodb_client()
    database = client[MONGODB_DATABASE]
    collection = database[collection_name]
    return collection
