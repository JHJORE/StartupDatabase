from tkinter import*
import customtkinter

from Components import NoteMenuBar, NavBar, NoteTree
from sql_app.models import Note
import requests

class Notes(Frame):

    def __init__(self, parent, controller,values):
        Frame.__init__(self, parent)
        self.OrgNumber = values[1]

        self.values = values
        # Frames
        top_frame = customtkinter.CTkFrame(self,
                                height= 200, 
                                corner_radius=0,
                            )
        top_frame.grid(row = 0, column = 0, sticky = "nswe")

        mid_frame = customtkinter.CTkFrame(self)
        mid_frame.grid(row = 1, column = 0, sticky = "nswe", padx = 10, pady = 10)

        tree_frame = customtkinter.CTkFrame(self)
        tree_frame.grid(row = 2, column = 0, sticky = "nswe", padx = 10, pady = 10)

        bottom_frame = customtkinter.CTkFrame(self)
        bottom_frame.grid(row = 3, column = 0, sticky = "nswe", padx = 10, pady = 10)

        self.title_entry = customtkinter.CTkEntry(bottom_frame,
                                 placeholder_text="Enter title",
                                width=150,
                                height=25,
                                border_width=2,
                                corner_radius=5)
        self.title_entry.grid(row = 0, column = 0, padx = 10, pady= 10, sticky = "w")

        self.textbox = Text(bottom_frame,width=112, height=10)
        self.textbox.grid(row = 1, column = 0, columnspan = 2)

        save_btn = customtkinter.CTkButton(bottom_frame, text="Save", command= self.add_note)
        save_btn.grid(row = 2, column=0, padx = 10, pady= 10)

        delete_btn = customtkinter.CTkButton(bottom_frame, text="Delete", command = self.delete_note)
        delete_btn.grid(row = 2, column=1, padx = 10, pady= 10)


      

        # menu
        
        self.navbar = NavBar.NavBar(parent, controller, top_frame)
        self.trash = NoteMenuBar.NoteMenuBar(parent,mid_frame, self.textbox, values)
        self.tree= NoteTree.NoteTree(self, tree_frame, self.OrgNumber, self.textbox, self.title_entry)


    def add_note(self):
        noteId = self.tree.get_noteId()

        if noteId == "":
            note = self.create_note()
            URL = "http://127.0.0.1:8000/Company/" + str(self.values[1]) + "/Note/"
            data = {"Name": note.Name, "Note": note.Note, "OrgNumber": note.OrgNumber}
            requests.post(url=URL, json=data)
        else:
            URL = "http://127.0.0.1:8000/Note/" + str(noteId) + "/update" 
            DATA = {"NoteId": int(noteId), "Name": self.title_entry.get(), "Note": self.textbox.get("1.0",'end-1c'), "OrgNumber": self.OrgNumber}
            requests.put(url=URL, json = DATA)
        
        self.tree.make_tree()


    def create_note(self):
        return Note(
            Name= self.title_entry.get(),
            Note = self.textbox.get("1.0",'end-1c'),
            OrgNumber = self.OrgNumber
        
        )

    def delete_note(self):
        noteId = self.tree.get_noteId()

        URL = "http://127.0.0.1:8000/Note/" + str(noteId) + "/delete"
        PARAMS = {"NoteId": noteId}
        requests.delete(url=URL, params=PARAMS)

        self.tree.delete_row(noteId)









