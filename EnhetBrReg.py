import json
from sql_app.models import Company
from sql_app import main
from sql_app import models
from sql_app.database import SessionLocal
import requests
import math

db = SessionLocal()

def create_list_orgnum():
    list_of_orgnum = ""
    companies = main.read_companies(db=db, limit=10000) #dette setter em limit på 10 000 selskaper vi får enhetsinformasjon fra
    for company in companies:
        list_of_orgnum += str(company.OrgNumber) + ","
    return math.ceil(len(companies)/20), list_of_orgnum[:-1]

def company_info_brreg():
    total_pages, list_of_orgnum = create_list_orgnum()
    
    for i in range(total_pages):
        request_url = "https://data.brreg.no/enhetsregisteret/api/enheter?organisasjonsnummer="
        request_url += list_of_orgnum
        request_url += "&page=" + str(i)
        print(request_url)
        response_API = requests.get(request_url)
        package_response = json.loads(response_API.text).get("_embedded").get("enheter")

        for package in package_response:
            company = main.read_Company(OrgNumber = package.get("organisasjonsnummer"), db=db)
            try:
                company.Description = package.get("naeringskode1").get("beskrivelse")
            except:
                pass
            company.Employees = package.get("antallAnsatte")
            company.Municipality = package.get("forretningsadresse").get("kommune")
            try:
                company.HomePage = package.get("hjemmeside")
            except:
                pass
            main.update_Company(OrgNumber=company.OrgNumber, Company=company, db=db)

company_info_brreg()
