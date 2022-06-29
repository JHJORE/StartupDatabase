import tkinter as tk
import customtkinter
from PIL import ImageTk, Image

class NavBar(tk.Frame):
    def __init__(self, parent, top_frame):
        tk.Frame.__init__(self, parent)

        folder_img = ImageTk.PhotoImage(Image.open("fi-og-img.png").resize((70,70),  Image.LANCZOS))
        icon = customtkinter.CTkButton(top_frame, image = folder_img,text="",borderwidth=0, width=70, height= 70, compound= "left" )
        icon.grid(row=0, column=0, padx=20, pady=10)

        folder_img = ImageTk.PhotoImage(Image.open("database.png").resize((40,40),  Image.LANCZOS))
        database_btn = customtkinter.CTkButton(top_frame, image = folder_img,text="", width=50, height= 50, compound= "left" )
        database_btn.grid(row=0, column=1, padx=10, )

        folder_img = ImageTk.PhotoImage(Image.open("company.png").resize((40,40),  Image.LANCZOS))
        company_btn = customtkinter.CTkButton(top_frame, image = folder_img,text="", width=50, height= 50, compound= "left" )
        company_btn.grid(row=0, column=2, padx=20, pady=10)

        folder_img = ImageTk.PhotoImage(Image.open("list.png").resize((40,40),  Image.LANCZOS))
        list_btn = customtkinter.CTkButton(top_frame, image = folder_img,text="", width=50, height= 50, compound= "left" )
        list_btn.grid(row=0, column=3, padx=20, pady=10)
