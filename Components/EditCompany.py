from tkinter import *
import customtkinter
from sql_app import models, main
from sql_app.database import SessionLocal
from Components import DeleteBox
from typing import Final
from Pages import Notes, NewsArticles

class EditCompany(Frame):
    
    def __init__(self, parent, bottom_frame, values, controller):
        Frame.__init__(self, parent)

        self.values = values
        self.controller = controller
        self.parent = parent
        self.db = SessionLocal()
        self.org_number = str(self.values[1])
        green : Final[str] = "#51B087"

        

        self.email_entry = customtkinter.CTkEntry(bottom_frame,
                                placeholder_text="Comany Email",
                               width=180,
                               height=25,
                               corner_radius=5)
        self.email_entry.grid(row=1, column=0,padx=10, pady=10)

        self.name_entry = customtkinter.CTkEntry(bottom_frame,
                                        placeholder_text="Company Name",
                                    width=180,
                                    height=25,
                                    border_width=2,
                                    corner_radius=5)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.org_label = customtkinter.CTkLabel(bottom_frame,corner_radius=50, text=self.org_number, bg_color=green)

        self.org_label.grid(row=0, column=0, padx=10, pady=10)
        

        self.employees_entry = customtkinter.CTkEntry(bottom_frame,
                                        placeholder_text="Employees",
                                    width=180,
                                    height=25,
                                    border_width=2,
                                    corner_radius=5)
        self.employees_entry.grid(row=1, column=1, padx=10, pady=10)

        self.description_entry = customtkinter.CTkEntry(bottom_frame,
                                        placeholder_text="Description",
                                    width=400,
                                    height=25,
                                    border_width=2,
                                    corner_radius=5)
        self.description_entry.grid(row=1, column=2,columnspan = 2, padx=10, pady=10)

        self.muncipality_entry = customtkinter.CTkEntry(bottom_frame,
                                        placeholder_text="Municipality",
                                    width=180,
                                    height=25,
                                    border_width=2,
                                    corner_radius=5)
        self.muncipality_entry.grid(row=0, column=2, padx=10, pady=10)

        update_btn = customtkinter.CTkButton(bottom_frame, text = 'Save Changes', command=self.update_company)
        update_btn.grid(row=3, column=0, columnspan=1, pady=10, padx=10, ipadx= 30 )

        notes_btn = customtkinter.CTkButton(bottom_frame, text="Notes", command= self.openNote)
        notes_btn.grid(row=3, column=1, columnspan=1, pady=10, padx=10, ipadx= 30 )

        news_btn = customtkinter.CTkButton(bottom_frame, text="News Articles", command= self.openNews)
        news_btn.grid(row=3, column=2, columnspan=1, pady=10, padx=10, ipadx= 30 )

        delete_btn = customtkinter.CTkButton(bottom_frame, text="Delete Company", command= self.openDelteBox)
        delete_btn.grid(row=3, column=3, columnspan=1, pady=10, padx=10, ipadx= 30 )

        self.name_entry.insert(0,values[0])
        self.email_entry.insert(0, values[2])
        self.muncipality_entry.insert(0, values[-1])
        self.description_entry.insert(0, values[4])
        self.employees_entry.insert(0, values[5])


 

    def update_company(self):
        company = self.create_company()
        OrgNumber = self.values[1]
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.muncipality_entry.delete(0, "end")
        self.employees_entry.delete(0, "end")
        self.description_entry.delete(0,"end")
        self.name_entry.insert(0, company.CompanyName)
        self.email_entry.insert(0, company.Email)
        self.muncipality_entry.insert(0, company.Municipality)
        self.org_label.insert(0,company.OrgNumber)
        self.employees_entry.insert(0, company.Employees)
        self.description_entry.insert(0,company.Description)
        main.update_Company(db=self.db, OrgNumber = OrgNumber, Company = company)
       


        
  


    def create_company(self):
        values = self.values

        return models.Company(
            OrgNumber = values[1],
            CompanyName = self.name_entry.get(),
            Email = self.email_entry.get(),
            Sector = values[3],
            Description = values[4],   
            Employees = self.employees_entry.get(),
            Municipality = self.muncipality_entry.get(),
            #HomePage = values[x],
        )
    def openNote(self):
        note_frame = Notes.Notes(self.parent.parent, self.controller,self.values)
        self.controller.show_frame(note_frame)

    def openNews(self):
        news_frame = NewsArticles.NewsArticles(self.parent.parent, self.controller, self.values[1])
        self.controller.show_frame(news_frame)

    def openDelteBox(self):
        if(self.values != ""):
            DeleteBox.DeleteBox(self.parent,self.values)
        
    