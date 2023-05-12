"""config.py contains the settings to setup up the application.
"""
from dotenv import load_dotenv
import os

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    """Config class"""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')\
            or 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
