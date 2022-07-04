import tkinter as tk
import customtkinter
from tkinter import ttk
from sqlalchemy import column, values
from sql_app.database import SessionLocal
import HomePage


class DatabaseApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
    
        container = customtkinter.CTkFrame(self)
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 
  
        frame = HomePage.HomePage(container, self)
        self.frames[frame] = frame 

        frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(frame)

    def show_frame(self, cont):
        cont.grid(row = 0, column = 0, sticky = "nsew")
        cont.tkraise()


app = DatabaseApp()
app.mainloop()
