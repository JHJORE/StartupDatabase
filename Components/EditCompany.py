import tkinter as tk
import customtkinter
from sql_app import models, main
import sqlite3
from sql_app.database import SessionLocal

class EditCompany(tk.Frame):
    def __init__(self, parent, bottom_frame, tree):
        tk.Frame.__init__(self, parent)

        self.db = SessionLocal()

        self.update_btn = customtkinter.CTkButton(bottom_frame, text = 'Save Changes', command=self.update_company)
        self.update_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx= 30 )

        self.remove_company_btn = customtkinter.CTkButton(bottom_frame, text="Remove Company", command= self.remove_company)
        self.remove_company_btn.grid(row=6, column=4, columnspan=2, pady=10, padx=10, ipadx= 30 )


        self.excel_btn = customtkinter.CTkButton(bottom_frame, text="Export to Excel", command= self.remove_company)
        self.excel_btn.grid(row=6, column=6, columnspan=2, pady=10, padx=10, ipadx= 30 )
        
        self.tree = tree

        self.email_entry = customtkinter.CTkEntry(bottom_frame,
                                placeholder_text="Company Email",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)
        self.email_entry.grid(row=0, column=5,padx=10, pady=10)

        self.name_entry = customtkinter.CTkEntry(bottom_frame,
                                    placeholder_text="Company Name",
                                width=180,
                                height=25,
                                border_width=2,
                                corner_radius=5)
        self.name_entry.grid(row=0, column=0, padx=10, pady=10)
        self.sector_edit = customtkinter.CTkEntry(bottom_frame,
                                placeholder_text="Municipality",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)
        self.sector_edit.grid(row=0, column=7,padx=10, pady=10)


    def update_company(self):
        select = self.tree.focus()
        row = self.tree.item(select)
        values = row.get('values')
        company = self.create_company()
        OrgNumber = values[1]
        self.tree.item(select, values=(company.CompanyName, company.OrgNumber, company.Email, company.Sector, company.Description, company.Employees, company.Municipality))
        main.update_Company(db=self.db, OrgNumber = OrgNumber, Company = company)


        
    def remove_company(self):
        select = self.tree.focus()
        row = self.tree.item(select)
        values = row.get('values')
        orgnumber = values[1]
        main.delete_Company(db = self.db, OrgNumber=orgnumber)
        
        company = self.tree.focus()
        self.tree.delete(company)

        

    def selected(self, values):
        self.email_entry.delete(0,tk.END) 
        self.sector_edit.delete(0,tk.END)
        self.name_entry.delete(0,tk.END)

        self.name_entry.insert(0,values[0])
        self.email_entry.insert(0, values[2])
        self.sector_edit.insert(0, values[-1])

    def create_company(self):
        select = self.tree.focus()
        row = self.tree.item(select)
        values = row.get('values')

        return models.Company(
            OrgNumber = values[1],
            CompanyName = self.name_entry.get(),
            Email = self.email_entry.get(),
            Sector = values[3],
            Description = values[4],   
            Employees = values[5],
            Municipality = self.sector_edit.get(),
            #HomePage = values[x],
        )
