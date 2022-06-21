import sqlite3

conn = sqlite3.connect("LeadsDatapool.db")

cursor = conn.cursor()

def insert_company(companyValues):
    OrgNumber = companyValues[0]
    statement = """INSERT INTO (OrgNumber, Name, ) Company VALUES (1000, Folkeinvest);"""
    conn.execute(statement)