import pandas as pd
import sqlite3
import csv

conn = sqlite3.connect("LeadsDatapool.db")
courser = conn.cursor()

df = pd.read_csv("TildelingerKopi.csv", encoding= "utf-8", delimiter=  ";")

# with open("Tildelinger.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)

#     df = pd.DataFrame([csv_reader], index= None)

#     # df.columns = ['thing']
#     df_split= df[].str.split(";")
#     print(df.to_string)
# # def fetch_data(df):
# #     for row in df:
        
#         Orgnumber = df[2]
#         CompanyName = df[3]
#         Sector = df[-2]
    
#         statement = """INSERT INTO Company (OrgNumber, CompanyName, Sector) VALUES (?, ?, ?)"""
#         courser.execute(statement, (Orgnumber, CompanyName, Sector))
#         conn.commit()


