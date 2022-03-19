# pylint: disable=raise-missing-from
from fastapi import HTTPException
from pymongo.errors import ExecutionTimeout
from src.databases.mongodb import get_collection


def read_from_mongodb(collection_name: str, data_id: int) -> dict:
    """
     read data from mongodb filter
     args:
        - collection_name: str
        - data_id: dict {"id": 1234}
    """
    try:
        collection = get_collection(collection_name)
        query_result = collection.find_one({"id": data_id})
        if query_result is None:
            raise HTTPException(
                status_code=404, detail=f"Card ID {data_id} not found in our database")
        query_result.pop('_id')
        return query_result
    except ExecutionTimeout:
        raise ExecutionTimeout("Timeout when trying to reading data cosmos")


def write_many(collection_name: str, data: dict) -> None:
    """
        Write many to mongodb
        args:
            - collection_name: str
            - data: dict
    """
    try:
        collection = get_collection(collection_name)
        collection.insert_many(data)
    except ExecutionTimeout:
        raise ExecutionTimeout("Timeout when trying to read from cosmos")
