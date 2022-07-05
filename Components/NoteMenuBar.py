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

        self.title_entry = customtkinter.CTkEntry(top_frame,
                                 placeholder_text="Enter title",
                                width=90,
                                height=25,
                                border_width=2,
                                corner_radius=5)
        self.title_entry.grid(row = 0, column = 1, padx = 10, pady= 10)

        save_btn = customtkinter.CTkButton(top_frame, text="Save", command= self.add_Note)
        save_btn.grid(row = 0, column=2, padx = 10, pady = 10 )

        delete_btn = customtkinter.CTkButton(top_frame, text="Delete")
        delete_btn.grid(row = 0, column=3, padx = 10, pady = 10 )

    def add_Note(self):
        note = self.create_Note()
        main.create_Note(db=self.db, OrgNumber = self.orgNumber, Note=note )


    def create_Note(self):
        input = self.textbox.get("1.0",'end-1c')
        
        return models.Note(
            Name= self.title_entry.get(),
            Note = input,
            OrgNumber = self.orgNumber
        
        )




