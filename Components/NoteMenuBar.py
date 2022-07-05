from tkinter import*
import customtkinter
from sql_app import models, main
from sql_app.database import SessionLocal

class NoteMenuBar(Frame):
    def __init__(self, parent, top_frame, textbox, values ):
        Frame.__init__(self, parent)
        self.top_frame = top_frame
        self.textbox= textbox
        self.orgNumber = values[1]
        self.Name = str(values[0])
        self.db = SessionLocal()

        name_label = customtkinter.CTkLabel(top_frame,text=self.Name, bg_color="#51B087", corner_radius=8)
        name_label.grid(row = 0 , column= 0, padx = 10, pady = 10)


       




