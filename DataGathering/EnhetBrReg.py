import json
from this import d
from sql_app import main
from sql_app.database import SessionLocal
import requests

db = SessionLocal()

def create_list_orgnum():
    list_of_orgnum_strings = []
    company_count = main.get_company_count(db = db)
    companies = main.read_companies(db=db, limit=company_count, skip=0)
    list_of_orgnum_string = ""
    for i in range(company_count):
        if i % 880 == 0 and i != 0:
            list_of_orgnum_strings.append(list_of_orgnum_string[:-1])
            list_of_orgnum_string = ""
        list_of_orgnum_string += str(companies[i].OrgNumber) + ","
    return list_of_orgnum_strings

def get_total_pages(list_of_orgnum): 
    request_url = "https://data.brreg.no/enhetsregisteret/api/enheter?organisasjonsnummer="
    request_url += list_of_orgnum
    response_API = requests.get(request_url)
    package_info = json.loads(response_API.text).get("page")
    total_pages = package_info.get("totalPages")
    return total_pages


def company_info_brreg():
    list_of_orgnum_strings = create_list_orgnum()
    for list_of_orgnum in list_of_orgnum_strings:
        total_pages = get_total_pages(list_of_orgnum=list_of_orgnum)
        for i in range(total_pages):
            request_url = "https://data.brreg.no/enhetsregisteret/api/enheter?organisasjonsnummer="
            request_url += list_of_orgnum
            request_url += "&page=" + str(i)
            response_API = requests.get(request_url)
            package_response = json.loads(response_API.text).get("_embedded").get("enheter")

            for package in package_response:
                try:
                    company = main.read_Company(OrgNumber = package.get("organisasjonsnummer"), db=db)
                    if(company.CompanyName[-2:] == 'AS'):
                        try:
                            company.Employees = package.get("antallAnsatte")
                        except:
                            pass
                        try:
                            company.Municipality = package.get("forretningsadresse").get("kommune")
                        except:
                            pass
                        try:
                            company.HomePage = package.get("hjemmeside")
                        except:
                            pass
                        try:
                            company.Description = package.get("naeringskode1").get("beskrivelse")
                        except:
                            pass
                        
                        main.update_Company(OrgNumber=company.OrgNumber, Company=company, db=db)
                    else:
                        main.delete_Company(OrgNumber=company.OrgNumber, db = db)
                except:
                    pass


company_info_brreg()
