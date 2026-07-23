import os

class Config:
    HOST = os.getenv("DB_HOST")
    PORT = int(os.getenv("DB_PORT", 20684))
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    DATABASE = os.getenv("DB_DATABASE")

    SECRET_KEY = os.getenv("SECRET_KEY", "praktikum-flask-2026")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"