from tkinter import *
from tkinter.ttk import Treeview
import requests

class NoteTree(Frame):
    def __init__(self, parent, tree_frame, OrgNumber, textbox, title_entry):
        Frame.__init__(self, parent)

        self.OrgNumber = str(OrgNumber)
        self.textbox = textbox
        self.title_entry = title_entry
       

        vertical_scroll = Scrollbar(tree_frame)
        vertical_scroll.grid(row=0, column=1, sticky="ns",padx = 0, pady = 10 )

        self.tree = Treeview(tree_frame,height= 3 , yscrollcommand= vertical_scroll.set)
        self.tree.grid(row = 0, column = 0, sticky = "nswe",padx = 10, pady = 10, ipadx = 10)

        vertical_scroll.config(command = self.tree.yview)
        self.tree['column'] = (
        "Name",
        "Description"
        )

        #colums
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Name", anchor="w", width= 140, stretch= 20)
        self.tree.column("Description", anchor="w", width= 600, stretch= 20)


        #Headings
        self.tree.heading("#0", text= "", anchor= W)
        self.tree.heading("Name", text= "Name", anchor= W)
        self.tree.heading("Description", text= "Description", anchor= W)
     


        self.tree.tag_configure('oddrow',background="white")
        self.tree.tag_configure('evenrow',background="#51B087")

        self.make_tree()

        self.tree.bind("<Double-1>", self.open_note)

    def open_note(self, e):
        select = self.tree.focus()
        values = self.tree.item(select, "values")
        self.textbox.delete(1.0, END)
        self.textbox.insert(END, values[1])
        self.title_entry.delete(0, END)
        self.title_entry.insert(0, values[0])
        


    def make_tree(self):
        if len(self.tree.get_children()):
            for note in self.tree.get_children():
                self.tree.delete(note)

        URL = "http://127.0.0.1:8000/Note/Org/" + self.OrgNumber
        PARAMS = {"OrgNumber": self.OrgNumber}
        r = requests.get(url=URL, params=PARAMS)
        
        notes = r.json()
        
        count_color = 0
        for note in notes:
            if count_color %2 ==0:
                self.tree.insert(parent='', index= 'end', iid=note["NoteId"], text="", values=(note["Name"], note["Note"]), tags=('evenrow'))
            else:
                self.tree.insert(parent='', index= 'end', iid=note["NoteId"], text="", values=(note["Name"], note["Note"]), tags=(''))
    
            count_color +=1

    def get_noteId(self):
        return self.tree.focus()

    def delete_row(self, noteId):
        self.tree.delete(noteId)
