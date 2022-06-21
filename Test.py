from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

def fetch_website(url):
    try:
        page = requests.get(url)
        return page
    except Exception as e:
        raise e

def get_capital_date_and_size(obj):
    capital_page = fetch_website("https://w2.brreg.no/kunngjoring/" + obj["link"])
    capital_soup = BeautifulSoup(capital_page.content, "html.parser")
    
    date = capital_soup.findAll(text=re.compile("Foretaksregisteret *"))[1].split(" ")[1]
    obj["date"] = date

    amount = capital_soup.findAll(text=re.compile("NOK *"))[0].split(" ")[1].replace(".","").replace(",", ".")
    obj["amount"] = float(amount)

def fetch_capital_raises_by_org_num(orgnum):
    page = fetch_website("https://w2.brreg.no/kunngjoring/hent_nr.jsp?orgnr=" + str(orgnum))
    capital_raises = []

    soup = BeautifulSoup(page.content, "html.parser")
    capitals = soup.findAll("a")

    for capital in capitals:
        if capital.text == "Kapital":
            capital_raises.append({"link": capital["href"]})

    for raises in capital_raises:
        get_capital_date_and_size(raises)
    
    df = pd.DataFrame.from_dict(capital_raises)
    df['date'] = pd.to_datetime(df['date'], format="%d.%m.%Y")
    df["change"] = df["amount"].pct_change(-1)*100
    
    return df

df = fetch_capital_raises_by_org_num(916545061)
print(df)