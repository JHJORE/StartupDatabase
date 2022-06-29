from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter
from matplotlib import image

from sqlalchemy import column, values

from sql_app import main,models
import sqlite3
from sql_app import database

from sql_app.database import SessionLocal
db = SessionLocal()

bottom_frame = customtkinter.CTkFrame(root)
bottom_frame.grid(row = 3, column = 0, sticky = "nswe",padx = 20, pady = 20)

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

muncipality_entry = customtkinter.CTkEntry(bottom_frame,
                                placeholder_text="Municipality",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)
muncipality_entry.grid(row=1, column=2, padx=10, pady=10)

update_btn = customtkinter.CTkButton(bottom_frame, text = 'Save Changes', command=update_company)
update_btn.grid(row=3, column=0, columnspan=1, pady=10, padx=10, ipadx= 30 )

notes_btn = customtkinter.CTkButton(bottom_frame, text="Notes", command= remove_company)
notes_btn.grid(row=3, column=1, columnspan=1, pady=10, padx=10, ipadx= 30 )

news_btn = customtkinter.CTkButton(bottom_frame, text="News Articles", command= remove_company)
news_btn.grid(row=3, column=2, columnspan=1, pady=10, padx=10, ipadx= 30 )

excel_btn = customtkinter.CTkButton(bottom_frame, text="Export to Excel", command= remove_company)
excel_btn.grid(row=3, column=3, columnspan=1, pady=10, padx=10, ipadx= 30 )
