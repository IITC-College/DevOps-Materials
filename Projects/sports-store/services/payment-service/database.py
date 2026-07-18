from motor.motor_asyncio import AsyncIOMotorClient
from os import environ
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = environ.get("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client["payment_db"]
payments_collection = db["payments"]
