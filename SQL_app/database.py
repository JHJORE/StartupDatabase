import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


from sqlalchemy import create_engine
from sqlalchemy.engine import URL

import urllib

params = 'DRIVER={ODBC Driver 18 for SQL Server};' \
         'SERVER=tcp:folkeinvest-internship2022.database.windows.net;' \
         'PORT=1433;' \
         'DATABASE=Folkeinvest-Internship-2022;' \
         'UID=Folkeinterns;' \
         'PWD=virtual_broom_bespoken_BLUFF;'
            
params = urllib.parse.quote_plus(params)

engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine)