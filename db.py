from datetime import datetime

from main import collection


class MongoDB:
    _collection = collection

    @classmethod
    async def get_data(cls, start_dt: datetime, end_dt: datetime):
        cursor = cls._collection.find({"dt": {"$gte": start_dt, "$lt": end_dt}})
        return [obj async for obj in cursor]

    @classmethod
    async def get_filter_aggregate_data(cls, start_dt: datetime, end_dt: datetime):
        pipline = [
            {"$match": {"dt": {"$gte": start_dt, "$lt": end_dt}}},
            {"$group": {"_id": start_dt, "total": {"$sum": "$value"}}}
        ]
        cursor = cls._collection.aggregate(pipline)
        return [obj async for obj in cursor]

    @classmethod
    async def insert_data(cls, data):
        await cls._collection.insert_many(data)
