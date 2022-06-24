from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "sqlite://folkeinvest-internship2022.database.windows.net"

# server = 'serverName\instanceName,port' # to specify an alternate port
# database = 'mydb' 
# username = 'myusername' 
# password = 'mypassword'

# params = quote_plus("Driver={ODBC Driver 13 for SQL Server};Server=tcp:folkeinvest-internship2022.database.windows.net,1433;Database=Folkeinvest-Internship-2022;Uid=Folkeinterns;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

# engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

#engine = create_engine("mssql+pyodbc://tcp:folkeinvest-internship2022.database.windows.net/Folkeinvest-Internship-2022?driver={ODBC Driver 13 for SQL Server}?pwd=virtual_broom_bespoken_BLUFF?Encryption=yes?TrustServerCertificate=no?Connection_Timeout=30")
engine = create_engine(
         SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# engine = create_engine("tcp:folkeinvest-internship2022.database.windows.net,1433;Database=Folkeinvest-Internship-2022;Uid=Folkeinterns;Pwd=virtual_broom_bespoken_BLUFF;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
