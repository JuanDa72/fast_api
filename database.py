#Import os to read environment variables
import os

#import create_engine to create a connection to the database
from sqlalchemy import create_engine

#import declarative_base to create the base class for our models
from sqlalchemy.ext.declarative import declarative_base

#import sessionmaker to create a session for our database operations
from sqlalchemy.orm import sessionmaker

DB_HOST=os.getenv("DB_HOST", "127.0.0.1")
DB_NAME=os.getenv("MYSQL_DATABASE", "books_db")
DB_PASSWORD=os.getenv("MYSQL_ROOT_PASSWORD", "root_password")
