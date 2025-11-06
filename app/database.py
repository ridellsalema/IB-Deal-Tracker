from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv("MSSQL_SERVER")
database = os.getenv("MSSQL_DATABASE")
username = os.getenv("MSSQL_USER")
password = os.getenv("MSSQL_PASSWORD")
driver = os.getenv("MSSQL_DRIVER")

# SQLAlchemy connection URL format for MSSQL
SQLALCHEMY_DATABASE_URL = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
