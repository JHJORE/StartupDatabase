import pandas as pd
import os

def save_as_excel(tree):
    
    OrgNumberList = []
    CompanyNameList = []
    EmailList = []
    SectorList = []
    DescriptionList = []
    EmployeesList = []
    MunicipalityList = []

    for company in tree.get_children():
        values = tree.item(company, "values")
        OrgNumberList.append(values[1])
        CompanyNameList.append(values[0])
        EmailList.append(values[2])
        SectorList.append(values[3])
        DescriptionList.append(values[4])
        EmployeesList.append(values[5])
        MunicipalityList.append(values[6])
    
    df = pd.DataFrame(
        {
            "OrgNumber": OrgNumberList,
            "CompanyName": CompanyNameList,
            "Email": EmailList,
            "Sector": SectorList,
            "Description": DescriptionList,
            "Employees": EmployeesList,
            "Municipality": MunicipalityList
        }
    )
    #print(df)
    if os.name == "nt":
        DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads\\"
    else:  # PORT: For *Nix systems
        DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads/"


    writer = pd.ExcelWriter(DOWNLOAD_FOLDER + "companies.xlsx")
    df.to_excel(writer)
    writer.save()


