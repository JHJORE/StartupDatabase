import pandas as pd
import os



def create_aid_df(aidtree):
    sum_list = []
    given_by_list = []
    type_list = []
    reason_list = []
    county_list = []
    date_given_list = []

    for aid in aidtree.get_children():
        values = aidtree.item(aid, "values")
        sum_list.append(values[0])
        given_by_list.append(values[1])
        type_list.append(values[2])
        reason_list.append(values[3])
        county_list.append(values[4])
        date_given_list.append(values[5])

    return pd.DataFrame(
        {
            "Sum": sum_list,
            "GivenBy": given_by_list,
            "Type": type_list,
            "Reason": reason_list,
            "County": county_list,
            "DateGiven": date_given_list
        }
    )


def create_capital_df(capitaltree):
    sum_list = []
    link_list = []
    date_list = []

    for aid in capitaltree.get_children():
        values = capitaltree.item(aid, "values")
        sum_list.append(values[0])
        date_list.append(values[1])
        link_list.append(values[2])

    return pd.DataFrame(
        {
            "Sum": sum_list,
            "Date": date_list,
            "Link": link_list
        }
    )

def create_company_df(values):
    return pd.DataFrame(
        {
            "OrgNumber": [values[1]],
            "CompanyName": [values[0]],
            "Sector": [values[3]],
            "Description": [values[4]],
            "Employees": [values[5]],
            "Municipality": [values[6]]
        }
    )

def save_as_excel(values, aidtree, capitaltree):
    
    company_df = create_company_df(values)
    aid_df = create_aid_df(aidtree)
    capital_df = create_capital_df(capitaltree)

    if os.name == "nt":
        DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads\\"
    else:  # PORT: For *Nix systems
        DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads/"


    writer = pd.ExcelWriter(DOWNLOAD_FOLDER + "company.xlsx")
    company_df.to_excel(writer, sheet_name="CompanyInfo")
    aid_df.to_excel(writer, sheet_name="Aid")
    capital_df.to_excel(writer, sheet_name="CapitalRaises")
    writer.save()

