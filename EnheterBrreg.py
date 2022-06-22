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

def enheter_json():
    


    with open('enheter_alle.json') as json_file:
        enheter = json.load(json_file)
    for package in enheter:
        kode = package.get("organisasjonsform").get("kode")
        if(kode !="AS" or package.get("konkurs")!= True):
            continue
        OrgNumber = package.get("organisasjonsnummer")
        CompanyName = package.get("navn")
        Description = package.get("beskrivelse")
        Sector = package.get("naeringskode1").get("naeringBeskrivelse") 
        Employees = package.get("antallAnsatte" )
        Municipality = package.get("forretningsadresse").get("kommune")

        company = Company(OrgNumber = OrgNumber,
        CompanyName = CompanyName,
        Sector = Sector,
        Description = Description,
        Employees = Employees,
        Municipality = Municipality) 
    
enheter_json()