
import json
from sql_app.models import Company




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