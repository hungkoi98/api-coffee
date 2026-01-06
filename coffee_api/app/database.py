from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = (
    "mssql+pyodbc://hung_admin:hugnkoi98@#@hungmssql.database.windows.net/coffee_db"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()