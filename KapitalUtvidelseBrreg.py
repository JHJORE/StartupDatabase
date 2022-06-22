
from urllib import response
import json
from pydantic import EmailError
import requests
from sqlalchemy import null
import sql_app
from sql_app import database
from sql_app.crud import create_Company
from sql_app.models import Company
from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3


def response_API():
    conn = sqlite3.connect("LeadsDatapool.db")
    courser = conn.cursor()
    # DB_URL = "http://127.0.0.1:8000/docs"
  
    # engine = create_engine("sqlite:///database.db")

  
   


    response_API = requests.get('https://data.brreg.no/rofs/od/rofs/stottetildeling/search?language=nob&mottakerOrgnr=987&fraDato=2020-11-20')
    package_response = json.loads(response_API.text)
    # db = local_session()
    database = []

    for package in package_response:
        OrgNumber = package.get("stottemottakerOrganisasjonsnummer")
        CompanyName = package.get("stottemottakerNavn")
    
        Sector = package.get("naeringBeskrivelse")
        company = Company(OrgNumber = OrgNumber,
        CompanyName = CompanyName,
        Sector = Sector) 
            
        print(company.OrgNumber)
        
        
response_API()
        
