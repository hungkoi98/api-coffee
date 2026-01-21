from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

password = quote_plus("hugnkoi98@#")
DATABASE_URL = (
    f"mssql+pyodbc://hung_admin:{password}"
    f"@hungmssql.database.windows.net:1433/qlkh"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&Encrypt=yes"
    "&TrustServerCertificate=no"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()