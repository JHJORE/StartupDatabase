from posixpath import split
import pandas as pd
import csv

from sqlalchemy import true

from sql_app.models import Company


df = pd.read_csv("TildelingerKopi.csv", encoding="ISO-8859-1")
s = 'Fylkesnavn;Kommunenavn;Org-nr;Bedriftsnavn;Virkemiddelkategori;Underkategori;Innvilget beløp;Innvilget dato;Beslutningsenhet;Næringshovedområde;Næring;Type finansiering'
df[s]=df[s].str.split(";")
df = df.explode(s).reset_index(drop=True)
# pivot = df.pivot_table('company',['Fylke', ' kommune', 'Org-nr', 'Navn','Virkemiddel', 'Under', 'innvilget', 'Belop', ' data', 'besluting', 'Naering','Ntype','finasiering'])
df.insert(1,'Bedriftnavn', '')
new_df = pd.DataFrame({s:df[s].iloc[::2].values, 'Bedriftnavn':df[s].iloc[1::2].values})

# for index, row in df.iterrows():
#     print(row[s])
#     compan = Company(OrgNumber = OrgNumber,
#         CompanyName = CompanyName,
        
#         Description = Description,
#         Employees = Employees,
#         Municipality = Municipality,
#         Sum = Sum)
print(df)


