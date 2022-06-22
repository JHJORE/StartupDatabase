import pandas as pd
import csv

with open("TildelingerKopi.csv", encoding="ISO-8859-1") as csv_file:
    csv_reader = csv.reader(csv_file)

    df = pd.DataFrame([csv_reader], index= None)
    
print(df)
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


