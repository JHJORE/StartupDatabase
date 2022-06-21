import sqlite3;


conn = sqlite3.connect("LeadsDatapool.db")

conn.execute("PRAGMA foreign_keys = ON;")

stmt = """CREATE TABLE Company (
    OrgNumber INTEGER NOT NULL,
    CompanyName TEXT NOT NULL,
    Email TEXT NOT NULL,
    Sector TEXT,
    CONSTRAINT PK_Company PRIMARY KEY (OrgNumber)
);"""

stmt2 = """CREATE TABLE Notes (
    NoteId INTEGER NOT NULL,
    Notes TEXT,
    OrgNumber INTEGER NOT NULL,
    CONSTRAINT PK_Notes PRIMARY KEY (NoteId),
    CONSTRAINT FK_Notes FOREIGN KEY (OrgNumber) REFERENCES Company(OrgNumber)
);"""

stmt3 = """CREATE TABLE NewsArticles(
    ArticleId INTEGER NOT NULL,
    URL TEXT NOT NULL,
    Title TEXT,
    OrgNumber INTEGER NOT NULL,
    CONSTRAINT PK_NewArticles PRIMARY KEY (ArticleId),
    CONSTRAINT FK_NewArticles FOREIGN KEY (OrgNumber) REFERENCES Company(OrgNumber)
);"""

stmt4 = """CREATE TABLE StockHolders(
    StockHolderId INTEGER NOT NULL,
    Name TEXT,
    OrgNumber INTEGER NOT NULL,
    CONSTRAINT PK_StockHolder PRIMARY KEY (StockHolderId),
    CONSTRAINT FK_Stockholder FOREIGN KEY (OrgNumber) REFERENCES Company(OrgNumber)
);"""
conn.execute(stmt4)

cursor = conn.cursor()
