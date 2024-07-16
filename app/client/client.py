from pymongo import MongoClient
import os
from motor.motor_asyncio import AsyncIOMotorClient

db_client = os.getenv("MONGO_DETAILS", "mongodb+srv://gastonhromero7:Messi41175282@cluster0.pu03jpc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = AsyncIOMotorClient(db_client)
database = client.test
user_collection = database.get_collection("users")