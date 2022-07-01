import tkinter as tk
import customtkinter
from tkinter import ttk
from sqlalchemy import column, values
from sql_app.database import SessionLocal
import HomePage, CompanyView, Notes


class DatabaseApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
        # WIDTH = 850
        # HEIGHT = 500


        # root = customtkinter.CTk()
        # root.title('Startup Database')
        # root.geometry(f"{WIDTH}x{HEIGHT}")

        # root.columnconfigure((0), weight=1)
        # root.rowconfigure((1,2,3,4,5,6,7,8,9), weight=1)
    
        container = customtkinter.CTkFrame(self)
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 
  

        print("h")
        frame = HomePage.HomePage(container, self)
        self.frames[frame] = frame
        print(frame)
        print(self.frames)
        frame.grid(row = 0, column = 0, sticky ="nsew")

        
        # homeframe = HomePage.HomePage(container, self)
        # self.frames[homeframe] = homeframe
        # homeframe.grid(row = 0, column = 0, sticky= "nsew")

        # homeframe = HomePage.HomePage(container, self, values)
        # self.frames[homeframe] = homeframe
        # homeframe.grid(row = 0, column = 0, sticky= "nsew")
  
        self.show_frame(frame)
        print("h")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def add_frame(self, cont):
        self.frames[cont] = cont
        cont.grid(row = 0, column = 0, sticky = "nsew")


app = DatabaseApp()
app.mainloop()
