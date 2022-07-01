from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import requests

from sql_app.models import Company

class NewFilter(Frame):
    def __init__(self, parent, search_frame, tree):
        Frame.__init__(self, parent)

        search_frame.rowconfigure((10), weight=1)

        self.companyname_entry = customtkinter.CTkEntry(search_frame,
                                placeholder_text="Company Name",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)

        self.companyname_entry.grid(row=0, column=0, padx=10, pady=10)  

        self.sector_entry = customtkinter.CTkEntry(search_frame,
                                placeholder_text="Sector",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)

        self.sector_entry.grid(row=0, column=1, padx=10, pady=10)  
        
        self.municipality_entry = customtkinter.CTkEntry(search_frame,
                                placeholder_text="Municipality",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)

        self.municipality_entry.grid(row=0, column=2, padx=10, pady=10)  




        self.folder_img = ImageTk.PhotoImage(Image.open("./Constants/searchicon.png").resize((20,20),  Image.LANCZOS))
        
        self.search_button = customtkinter.CTkButton(search_frame, image = self.folder_img,text="", width=20, height= 20, compound= "left", command=self.search_database)
        self.search_button.grid(row=0, column=5, padx=10, pady=10)

        self.employee_entry1 = customtkinter.CTkEntry(search_frame,
                                    placeholder_text="MinEmployees",
                                width=180,
                                height=25,
                                border_width=2,
                                corner_radius=5)
        self.employee_entry1.grid(row=1, column=0, padx=10, pady=10)
    
        self.employee_entry2 = customtkinter.CTkEntry(search_frame,
                                    placeholder_text="MaxEmployees",
                                width=180,
                                height=25,
                                border_width=2,
                                corner_radius=5)
        self.employee_entry2.grid(row=1, column=1, padx=10, pady=10)

        delete_btn = customtkinter.CTkButton(search_frame, text="Delete Company", command= self.remove_company)
        delete_btn.grid(row=1, column=2, columnspan=1, pady=10, padx=10, ipadx= 30, sticky="ne")

        self.tree = tree

    def search_database(self):
        CompanyName = self.companyname_entry.get()
        Sector = self.sector_entry.get()
        EmployeesMin = 0 if self.employee_entry1.get() == "" else self.employee_entry1.get()
        EmployeesMax = 1000000 if self.employee_entry2.get() == "" else self.employee_entry2.get()
        Municipality = self.municipality_entry.get()


        URL = "http://127.0.0.1:8000/Company/"
        # sett inn i PARAMS når det går: "CompanyName": CompanyName,
        PARAMS = {"Sector": Sector, "EmployeesMin": EmployeesMin, "EmployeesMax": EmployeesMax, "Municipality": Municipality}

        r = requests.get(url = URL, params = PARAMS)
        companies = r.json()
        self.make_treeview(companies)

    def make_treeview(self, companies):
        for company in self.tree.get_children():
                self.tree.delete(company)
        count_color = 0
        for company in companies:
            if count_color %2 ==0:
                self.tree.insert(parent='', index= 'end', iid=company["OrgNumber"], text="", values=(company["CompanyName"],company["OrgNumber"],company["Email"],company["Sector"],company["Description"],company["Employees"],company["Municipality"]), tags=('evenrow'))
            else:
                self.tree.insert(parent='', index= 'end', iid=company["OrgNumber"], text="", values=(company["CompanyName"],company["OrgNumber"],company["Email"],company["Sector"],company["Description"],company["Employees"],company["Municipality"]), tags=(''))
            count_color +=1
    
    def remove_company(self):
        company = self.tree.focus()
        row = self.tree.item(company)
        values = row.get('values')
        orgnumber = values[1]
        self.tree.delete(company)

        URL = "http://127.0.0.1:8000/Company/" + str(orgnumber) + "/delete"
        PARAMS = {"OrgNumber": orgnumber}
        requests.delete(url = URL, params = PARAMS)
