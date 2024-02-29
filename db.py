from main import collection


class MongoDB:
    _collection = collection

    @classmethod
    async def insert_data(cls, data):
        await cls._collection.insert_many(data)
