from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from click import command
import customtkinter
from matplotlib import image
from matplotlib.pyplot import text
from tkinter import filedialog
from Components import files_view

from sqlalchemy import column, false, values
from sql_app import main,models
import sqlite3
from sql_app import database

from sql_app.database import SessionLocal
db = SessionLocal()

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
WIDTH = 920
HEIGHT = 700


root = customtkinter.CTk()
root.title('Startup Database')
root.geometry(f"{WIDTH}x{HEIGHT}")
conn = sqlite3.connect('sql_app.db')
cursor = conn.cursor()

root.columnconfigure((0), weight=1)
root.rowconfigure((1,2,3,4,5,6,7,8,9), weight=1)


#Style
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
foreground ="black",
rowheight = 23,
)

# Frames
top_frame = customtkinter.CTkFrame(root,
                        height= 30, 
                        corner_radius=0,
                    )
top_frame.grid(row = 0, column = 0, sticky = "nswe")

title_frame = customtkinter.CTkFrame(root)
title_frame.grid(row = 1, column = 0, sticky = "nswe", padx = 20, pady = 10)

bottom_frame = customtkinter.CTkFrame(root)
bottom_frame.grid(row = 2, column = 0, sticky = "nswe", padx = 20, pady = 10)

#menu

cas = files_view.files_view(root, root)

title = customtkinter.CTkLabel(master=top_frame,
                               width=120,
                               text="Company Name",
                               height=45,
                               corner_radius=8)
title.grid(row =0, column= 0)



#Scrollbar
vscroll = Scrollbar(bottom_frame)
vscroll.pack(side=RIGHT, fill= Y)

textbox = Text(bottom_frame,width=200, height=200)
textbox.pack()

vscroll.config(command=textbox.yview)

conn.commit()
conn.close()
root.mainloop()