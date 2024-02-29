import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient()
db = client["main_db"]
collection = db["rlt_test_collection"]
