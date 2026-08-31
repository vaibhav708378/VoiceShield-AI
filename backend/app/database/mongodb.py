from pymongo import MongoClient
from app.core.config import settings


class MongoDB:
    client = MongoClient(settings.MONGODB_URL)
    database = client[settings.DATABASE_NAME]


mongodb = MongoDB()

db = mongodb.database