from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mssql+pyodbc://<username>:<password>@<hostname>/<database>?driver=ODBC+Driver+17+for+SQL+Server"

# engine = create_engine(DATABASE_URL, pool_size=5, max_overflow=10)
engine = create_engine(
    DATABASE_URL,
    pool_size=5,  # Set the desired pool size
    max_overflow=10,  # Set the maximum number of connections allowed to overflow
    pool_pre_ping=True,  # Enable connection validation before usage
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()