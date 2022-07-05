from tkinter import *

from sql_app.crud import create_Note

class FilesView(Frame):
    def __init__(self, parent, top_frame, current_note):
        Frame.__init__(self, parent)
        notes_menu = Menu(top_frame)
        top_frame.config(menu= notes_menu)

        file_menu = Menu(notes_menu, tearoff=False)
        notes_menu.add_cascade(label="Files", menu= file_menu)
        file_menu.add_command(label="New", command= self.new_note())
        file_menu.add_command(label="Open", command= self.open_note())
        file_menu.add_command(label="Delete", command= self.delete_note())
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command= top_frame.quit)
      

        edit_menu = Menu(notes_menu, tearoff=False)
        notes_menu.add_cascade(label="Files", menu= edit_menu)
        edit_menu.add_command(label="Save")
        edit_menu.add_command(label="Redu")
        edit_menu.add_command(label="Undo")
        
       

        status_bar = Label(top_frame, text= "Ready     ", anchor=E)
        status_bar.grid(row=0,column=3, padx=10, pady=10, sticky="NE" )


    def new_note(self):
        self.current_note.delete("1.0", END)
        self.top_frame.title('New File - Note')
        self.status_bar.config(text= "New File        ")

    def open_note(self):
        self.current_note.delete("1.0", END)

    def create_note():
        pass

        
    def delte_note(self):
        pass
    