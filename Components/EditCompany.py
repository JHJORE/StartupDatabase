import tkinter as tk
import customtkinter
from sql_app import models, main
import sqlite3
from sql_app.database import SessionLocal

class EditCompany(tk.Frame):
    def __init__(self, parent, bottom_frame, tree):
        tk.Frame.__init__(self, parent)

        self.db = SessionLocal()

        email_entry = customtkinter.CTkEntry(bottom_frame,
                                placeholder_text="Comany Email",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)
        email_entry.grid(row=1, column=0,padx=10, pady=10)

        # company_name = customtkinter.CTkLabel(bottom_frame, text="Name", width=180,height=25, corner_radius=8)
        # company_name.grid(row=0, column= 0,  padx=10, pady=10)

        name_entry = customtkinter.CTkEntry(bottom_frame,
                                        placeholder_text="Company Name",
                                    width=180,
                                    height=25,
                                    border_width=2,
                                    corner_radius=5)
        name_entry.grid(row=0, column=0, padx=10, pady=10)

        org_entry = customtkinter.CTkEntry(bottom_frame,
                                        placeholder_text="OrgNumber",
                                    width=180,
                                    height=25,
                                    border_width=2,
                                    corner_radius=5)
        org_entry.grid(row=0, column=1, padx=10, pady=10)

        name_entry = customtkinter.CTkEntry(bottom_frame,
                                        placeholder_text="Employees",
                                    width=180,
                                    height=25,
                                    border_width=2,
                                    corner_radius=5)
        name_entry.grid(row=1, column=1, padx=10, pady=10)

        muncipality_entry = customtkinter.CTkEntry(bottom_frame,
                                        placeholder_text="Municipality",
                                    width=180,
                                    height=25,
                                    border_width=2,
                                    corner_radius=5)
        muncipality_entry.grid(row=1, column=2, padx=10, pady=10)

        update_btn = customtkinter.CTkButton(bottom_frame, text = 'Save Changes', command=self.update_company)
        update_btn.grid(row=3, column=0, columnspan=1, pady=10, padx=10, ipadx= 30 )

        notes_btn = customtkinter.CTkButton(bottom_frame, text="Notes")#, command= self.notes)
        notes_btn.grid(row=3, column=1, columnspan=1, pady=10, padx=10, ipadx= 30 )

        news_btn = customtkinter.CTkButton(bottom_frame, text="News Articles")#, command= self.news)
        news_btn.grid(row=3, column=2, columnspan=1, pady=10, padx=10, ipadx= 30 )

        delete_btn = customtkinter.CTkButton(bottom_frame, text="Delete Company", command= self.remove_company)
        delete_btn.grid(row=3, column=3, columnspan=1, pady=10, padx=10, ipadx= 30 )


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
