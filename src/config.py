import os

from dotenv import load_dotenv

load_dotenv()


class FlaskConfig:
    HOST = os.getenv("FLASK_HOST", "0.0.0.0")
    PORT = int(os.getenv("FLASK_PORT", 5000))
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() in ("1", "true", "yes")


class MongoConfig:
    URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/problems")
    DB_NAME = os.getenv("MONGO_DB_NAME", "problems")
    COLL_NAME = os.getenv("MONGO_COLLECTION_NAME", "problems")
    WRITE_CONCERN = {"w": "majority", "journal": True}