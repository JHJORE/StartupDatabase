import tkinter as tk

from tkinter import ttk
from sqlalchemy import column, values
from sql_app.database import SessionLocal
import HomePage, CompanyView, Notes


class DatabaseApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
    
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 
  

        for F in (HomePage, CompanyView):
  
            frame = F(container, self)
  

            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(HomePage)
  

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = DatabaseApp()
app.mainloop()
