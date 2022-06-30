from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from sql_app.database import SessionLocal
import sqlite3

class Filter(Frame):
    def __init__(self, parent, search_frame, tree):
        Frame.__init__(self, parent)

        self.db = SessionLocal()

        self.search_entry = customtkinter.CTkEntry(search_frame,
                                placeholder_text="Search Company",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)

        self.search_entry.grid(row=0, column=0, padx=10, pady=10)  


        self.folder_img = ImageTk.PhotoImage(Image.open("searchicon.png").resize((20,20),  Image.LANCZOS))
        self.search_button = customtkinter.CTkButton(search_frame, image = self.folder_img,text="", width=20, height= 20, compound= "left", command=self.search_database)
        self.search_button.grid(row=0, column=5, padx=10, pady=10)
        self.search_dropdown = customtkinter.CTkOptionMenu(search_frame,
                                                        values=["CompanyName",
                                                        "OrgNumber", 
                                                        "Sector", 
                                                        "Employees", 
                                                        "Municipality"],
                                                        command=self.check_dropdown,
                                                    )
        self.search_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.employee_entry1 = customtkinter.CTkEntry(search_frame,
                                    placeholder_text="Start",
                                width=60,
                                height=25,
                                border_width=2,
                                corner_radius=5)
        self.employee_entry2 = customtkinter.CTkEntry(search_frame,
                                    placeholder_text="End",
                                width=60,
                                height=25,
                                border_width=2,
                                corner_radius=5)

        self.tree = tree

    def check_dropdown(self, x):
        if(x == "Employees"):
            self.employee_entry1.grid(row=0, column=2, padx=10, pady=10)
            self.employee_entry2.grid(row=0, column=3, padx=10, pady=10)
        else:
            self.employee_entry1.grid_remove()
            self.employee_entry2.grid_remove()

    def search_database(self):
        conn = sqlite3.connect('sql_app.db')
        cursor = conn.cursor()
        filter = self.search_dropdown.get()
        company_search = self.search_entry.get()
        cursor.execute("SELECT *, oid FROM Company ")
        companies = cursor.fetchall()
        if(company_search != ""): 
            for company in self.tree.get_children():
                self.tree.delete(company)
            company_search = "%" + company_search + "%"
            cursor.execute(f"SELECT *, oid FROM Company WHERE {filter} like ?", (company_search,))
            companies = cursor.fetchall()
            self.make_treeview(companies)
        else:
            for company in self.tree.get_children():
                self.tree.delete(company)
            if(filter == "Employees"): #trenges ettersom vi sorterer i tall og ikke items
                self.employee_treeview(companies)
            else:
                self.make_treeview(companies) 
        conn.commit()
        conn.close()

    def make_treeview(self, companies):
        count_color = 0
        for company in companies:
            if count_color %2 ==0:
                self.tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=('evenrow'))
            else:
                self.tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=(''))
        
            count_color +=1

    def employee_treeview(self, companies):
        count_color = 0
        employees_start = int(self.employee_entry1.get())
        employees_end = int(self.employee_entry2.get())
        for company in companies:
            employed = company[5]
            if employed == None:
                continue
            if(employees_end>= employed and employed>=employees_start):
                if count_color %2 ==0:
                    self.tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=('evenrow'))
                else:
                    self.tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=(''))
        
                count_color +=1
