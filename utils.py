import bson

from db import MongoDB


async def insert_sample_collection(file: str) -> None:
    data = []
    with open(file, 'rb') as f:
        data_bson = f.read()
        data = bson.decode_all(data_bson)
    await MongoDB.insert_data(data)
