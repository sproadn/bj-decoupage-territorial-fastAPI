from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get database config from OS env
user = os.getenv('DB_MYSQL_USER')
password = os.getenv('DB_MYSQL_PASS')
host = os.getenv('DB_HOST')
port = os.getenv('DB_MYSQL_PORT')
db_name = os.getenv('DB_NAME')
hostname = f"{host}:{port}"


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@{hostname}/{db_name}"
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
