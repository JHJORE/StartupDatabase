import json
import pandas
import requests
from sql_app import models, main
from sql_app.database import SessionLocal
import pandas as pd

db = SessionLocal()

def brreg_tilsagn_to_db():  
    response_API = requests.get('https://data.brreg.no/rofs/od/rofs/stottetildeling/search?language=nob&mottakerOrgnr=987&fraDato=2016-11-20')
    package_response = json.loads(response_API.text)
    for package in package_response:
        OrgNumber = package.get("stottemottakerOrganisasjonsnummer")
        CompanyName = package.get("stottemottakerNavn")
        Sector = package.get("naeringBeskrivelse")
        givenBy = package.get("stottegiverNavn")
        typeOfAid = package.get("typeTiltak")
        reason = package.get("formaal")
        county = package.get("fylke")
        amountGiven = package.get("tildeltBelop")
        dateGiven = pd.to_datetime(package.get("tildelingsdato"), format= "%d.%m.%Y")
        aidId = package.get("stottemottakerOrganisasjonsnummer") + package.get("tildelingsdato")

        # dateinfo = package.get("tildelingsdato").split(".")
        # year, month, day = int("20" + dateinfo[0]), int(dateinfo[1]), int(dateinfo[2])
        # dateGiven = date(year, month, day)

        aid = models.Aid(
            AidId = aidId,
            Sum = amountGiven,
            OrgNumber = OrgNumber,
            Type = typeOfAid,
            GivenBy = givenBy,
            Reason = reason,
            DateGiven = dateGiven,
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

        
        
brreg_tilsagn_to_db()
        
