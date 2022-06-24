
import json
from sql_app.models import Company
from sql_app import main
from sql_app import models
from sql_app.database import SessionLocal

db = SessionLocal()


# henter inn alle bedrifter i hele Norge
def enheter_json():
    db = SessionLocal()
    with open('enheter_alle.json', encoding="ISO-8859-1") as json_file:
        enheter = json.load(json_file)
    for package in enheter:
        kode = package.get("organisasjonsform").get("kode")
        if(kode !="AS" or package.get("konkurs")!= False):
            continue
        OrgNumber = package.get("organisasjonsnummer")
        CompanyName = package.get("navn")
        try:
            Description = package.get("naeringskode1").get("beskrivelse")

        except:
            Description = None
        else:
             Description = package.get("institusjonellSektorkode").get("beskrivelse")
        Employees = package.get("antallAnsatte" )
        Municipality = package.get("forretningsadresse").get("kommune")

        company = Company(OrgNumber = OrgNumber,
        CompanyName = CompanyName,
        
        Description = Description,
        Employees = Employees,
        Municipality = Municipality) 
        main.create_Company(Company=company, db = db)

        
    
enheter_json()





