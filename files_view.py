from tkinter import *
from tkinter.ttk import Treeview
from turtle import right
import customtkinter
from numpy import pad
from sql_app import models, main
import sqlite3

class files_view(Frame):
    def __init__(self, parent, top_frame):
        Frame.__init__(self, parent)
        notes_menu = Menu(top_frame)
        top_frame.config(menu= notes_menu)

        file_menu = Menu(notes_menu, tearoff=False)
        notes_menu.add_cascade(label="Files", menu= file_menu)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Delete")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command= top_frame.quit)
      

        edit_menu = Menu(notes_menu, tearoff=False)
        notes_menu.add_cascade(label="Files", menu= edit_menu)
        edit_menu.add_command(label="Save")
        edit_menu.add_command(label="Redu")
        edit_menu.add_command(label="Undo")
        
       

        status_bar = Label(top_frame, text= "status", anchor=E)
        status_bar.grid(row=0,column=3, padx=10, pady=10, sticky="NE" )