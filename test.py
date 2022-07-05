# from tkinter import Pack
# import requests
  
# # api-endpoint
# URL = "http://127.0.0.1:8000/Company/"
  
# # location given here
# location = "Oslo"
  
# # defining a params dict for the parameters to be sent to the API
# PARAMS = {'Municipality':location, "EmployeesMax": 100, "EmployeesMin": 10, "Sector": "helse"}
# PARAMS = {"Sector": "finans", "EmployeesMin": 0, "EmployeesMax": 100000, "Municipality": ""}

# # sending get request and saving the response as response object
# r = requests.get(url = URL, params=PARAMS)
  
# # extracting data in json format
# data = r.json()
# print(data)

# import sqlite3
# conn = sqlite3.connect("sql_app.db")
# cursor = conn.cursor()
# print(cursor.execute("select * from Note;").fetchall())
import requests

URL = "http://127.0.0.1:8000/Note/Org/" + str(898783472)
PARAMS = {"OrgNumber": 898783472}
r = requests.get(url=URL, params=PARAMS)

notes = r.json()
print(notes)