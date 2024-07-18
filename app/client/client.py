from pymongo import MongoClient
import os
MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb+srv://gastonhromero7:Messi41175282@cluster0.pu03jpc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient(MONGO_DETAILS)
database = client.get_database("test")
user_collection = database.get_collection("users")