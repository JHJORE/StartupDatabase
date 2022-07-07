import pandas as pd
from sql_app.models import Aid, Company
from sql_app import main
from sql_app.database import SessionLocal

db = SessionLocal()

def innovation_norway_help():
    df = pd.read_csv("DataGathering/Tildelinger.csv", encoding="ISO-8859-1", sep=";")
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    i = 0
    for row in df.iterrows():
        i += 1
        if (i % 1000 == 0):
            print(i)
        if len(str(int((row[1].loc["Org-nr"])))) != 9 or row[1].loc["Næringshovedområde"].lower() == "uspesifisert":
            continue

        OrgNumber = int(row[1].loc["Org-nr"])
        dateGivenString = row[1].loc["Innvilget dato"]
        dateGivenString = dateGivenString[:6] + "20" + dateGivenString[6:]
        dateGiven = pd.to_datetime(dateGivenString, format= "%d.%m.%Y")
        aidId = str(OrgNumber) + dateGivenString
        
        company = Company(
            OrgNumber = OrgNumber,
            CompanyName = row[1].loc["Bedriftsnavn"],
            Municipality = row[1].loc["Kommunenavn"],
            Sector = row[1].loc["Næringshovedområde"]
        )
        aid = Aid (
            Sum = row[1].loc["Innvilget beløp"],
            GivenBy = "Innovasjon Norge",
            Type = row[1].loc["Virkemiddelkategori"],
            Reason = row[1].loc["Virkemiddelkategori"],
            County = row[1].loc["Fylkesnavn"],
            DateGiven = dateGiven,
            AidId = aidId,
            OrgNumber = OrgNumber
        )


        try:
            main.read_Company(OrgNumber=OrgNumber, db=db)
            main.update_Company(OrgNumber = OrgNumber, Company=company, db = db)
            try:
                main.read_Aid(AidId = aidId, db=db)
                main.update_Aid(AidId = aidId, Aid=aid, db=db)
                
            except:
                main.create_Aid(OrgNumber=OrgNumber, Aid=aid, db=db)
        except:
            main.create_Company(Company=company, db= db)
            try:
                main.read_Aid(AidId = aidId, db=db)
                main.update_Aid(AidId = aidId, Aid=aid, db=db)
                
            except:
                main.create_Aid(OrgNumber=OrgNumber, Aid=aid, db=db)




innovation_norway_help()
