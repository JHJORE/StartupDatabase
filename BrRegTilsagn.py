import json
import requests
from sql_app import models, main
from sql_app.database import SessionLocal

db = SessionLocal()

def brreg_tilsagn_to_db():  
    response_API = requests.get('https://data.brreg.no/rofs/od/rofs/stottetildeling/search?language=nob&mottakerOrgnr=987&fraDato=2017-01-01')
    package_response = json.loads(response_API.text)

    for package in package_response:
        aidId = package.get("tildelingId")
        OrgNumber = package.get("stottemottakerOrganisasjonsnummer")
        CompanyName = package.get("stottemottakerNavn")
        Sector = package.get("naeringBeskrivelse")
        givenBy = package.get("stottegiverNavn")
        typeOfAid = package.get("typeTiltak")
        reason = package.get("formaal")
        county = package.get("fylke")
        amountGiven = package.get("tildeltBelop")

        aid = models.Aid(
            AidId = aidId,
            Sum = amountGiven,
            OrgNumber = OrgNumber,
            Type = typeOfAid,
            GivenBy = givenBy,
            Reason = reason,
            County = county
        )
        
        updated_company = models.Company(
            OrgNumber = OrgNumber,
            CompanyName = CompanyName,
            Sector = Sector,
        )


        try:
            main.read_Company(OrgNumber=OrgNumber, db=db)
            main.update_Company(OrgNumber = OrgNumber, Company=updated_company, db = db)
            try:
                main.read_Aid(AidId = aidId, db=db)
                main.update_Aid(AidId = aidId, Aid=aid, db=db)
                
            except:
                main.create_Aid(OrgNumber=OrgNumber, Aid=aid, db=db)
        except:
            main.create_Company(Company=updated_company, db= db)
            try:
                main.read_Aid(AidId = aidId, db=db)
                main.update_Aid(AidId = aidId, Aid=aid, db=db)
                
            except:
                main.create_Aid(OrgNumber=OrgNumber, Aid=aid, db=db)

        
        
response_API()
        
