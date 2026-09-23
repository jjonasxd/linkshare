import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    username = os.getenv("username")
    password = os.getenv("password")

class DevelopmentConfig:
    pass

class ProductionConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY")
