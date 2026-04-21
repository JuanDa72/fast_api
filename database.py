#Import os to read environment variables
import os

#import create_engine to create a connection to the database
from sqlalchemy import create_engine

#import declarative_base to create the base class for our models
from sqlalchemy.ext.declarative import declarative_base

#import sessionmaker to create a session for our database operations
from sqlalchemy.orm import sessionmaker

#To read the environment variables from the .env file, we can use the settings object from the config module
from config import settings

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://root:{settings.db_pass}"
    f"@{settings.db_host}:3306/{settings.db_name}"
)

engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()
    