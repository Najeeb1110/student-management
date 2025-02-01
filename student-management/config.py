import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_connection_string")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key")
