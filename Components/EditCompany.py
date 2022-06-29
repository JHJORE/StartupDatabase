import tkinter as tk
import customtkinter
from sql_app import models, main
import sqlite3

class EditCompany(tk.Frame):
    def __init__(self, parent, bottom_frame, tree):
        tk.Frame.__init__(self, parent)

        self.update_btn = customtkinter.CTkButton(bottom_frame, text = 'Save Changes', command=update_company)
        self.update_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx= 30 )

        self.remove_company_btn = customtkinter.CTkButton(bottom_frame, text="Remove Company", command= remove_company)
        self.remove_company_btn.grid(row=6, column=4, columnspan=2, pady=10, padx=10, ipadx= 30 )


        self.excel_btn = customtkinter.CTkButton(bottom_frame, text="Export to Excel", command= remove_company)
        self.excel_btn.grid(row=6, column=6, columnspan=2, pady=10, padx=10, ipadx= 30 )
        
        self.tree = tree
    
        tree['column'] = (
        "Name",
        "OrgNumber",
        "Email",
        "Sector",
        "Description",
        "Employees",
        "Manicipality")

    def create_company(self):
        select = self.tree.focus()
        row = self.tree.item(select)
        values = row.get('values')
        
        print(values[1])
        print(values[0])
        print(values[-1])

        return models.Company(
            OrgNumber = values[1],
            CompanyName = values[0],
            Description = values[-1],   
        )


    def update_company(self):
        select = self.tree.focus()
        row = self.tree.item(select)
        values = row.get('values')
        OrgNumber = values[1]

        main.update_Company(db=db, OrgNumber = OrgNumber, Company= create_company())

        
        

    def remove_company(orgnumber):
        conn = sqlite3.connect('sql_app.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Company WHERE OrgNumber = "+ orgNumber)
        conn.commit()
        conn.close()

        companies = self.tree.selection()
        for company in companies:
            orgNumber = company
            print(company)
            
            self.tree.delete(company)

        

    # def selected():
    #     email_entry.delete(0,END) 
    #     sector_edit.delete(0,END)
    #     name_entry.delete(0,END)

    #     select = tree.focus()
    #     row = tree.item(select)
    #     values = row.get('values')
        


    #     values = tree.item(select,'values')

    #     name_entry.insert(0,values[0])
    #     email_entry.insert(0, values[2])
    #     sector_edit.insert(0, values[-1])
