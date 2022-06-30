from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter
from sqlalchemy import column, values
import sqlite3
from sql_app.database import SessionLocal
import Components.capitalTree as capitalTree
import Components.aidTree as aidTree
db = SessionLocal()

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
WIDTH = 820
HEIGHT = 600


root = customtkinter.CTk()
root.title('Startup Database')
root.geometry(f"{WIDTH}x{HEIGHT}")
conn = sqlite3.connect('sql_app.db')
cursor = conn.cursor()

root.columnconfigure((0,1), weight=1)
root.rowconfigure((1,1), weight=1)
#Style
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
foreground ="black",
rowheight = 23,
)

#Frames
topp_frame = customtkinter.CTkFrame(root)
topp_frame.grid(row = 0, column = 0,  columnspan=2, sticky = "nswe", padx = 20, pady = 20)

left_frame = customtkinter.CTkFrame(root)
left_frame.grid(row = 1, column = 0, sticky = "nswe", padx = 20, pady = 10)

right_frame = customtkinter.CTkFrame(root)
right_frame.grid(row = 1, column = 1, sticky = "nswe", padx = 20, pady = 10)

#tree kapitalutvidelse
capitaltree = capitalTree.capitalTree(root, right_frame)


#tree AID
aid = aidTree.aidTree(root,left_frame)





# tree.bind("<ButtonRelease-1>", clicked)


conn.commit()
conn.close()

root.mainloop()