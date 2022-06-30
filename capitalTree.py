from tkinter import *
from tkinter.ttk import Treeview
from turtle import right
import customtkinter
from numpy import pad
from sql_app import models, main
import sqlite3

class capitalTree(Frame):
    def __init__(self, parent, right_frame):
        Frame.__init__(self, parent)
        conn = sqlite3.connect('sql_app.db')
        cursor = conn.cursor()


        vertical_scroll = Scrollbar(right_frame)
        vertical_scroll.grid(row=0, column=1, sticky="ns",padx = 0, pady = 40 )

        tree = Treeview(right_frame,height= 20 , yscrollcommand= vertical_scroll.set)
        tree.grid(row = 0, column = 0, sticky = "nswe",padx = 40, pady = 40, ipadx = 10)

        vertical_scroll.config(command = tree.yview)
        tree['column'] = (
        "Sum",
        "Date",
        "Link")

        #colums
        tree.column("#0", width=0, stretch=NO)
        tree.column("Sum", anchor=CENTER, width= 200, stretch= 20)
        tree.column("Date", anchor=W, width= 200, stretch= 20)
        tree.column("Link", anchor=W, width= 300, stretch= 20)

        #Headings
        tree.heading("#0", text= "", anchor= W)
        tree.heading("Sum", text= "Sum", anchor= W)
        tree.heading("Date", text= "Date", anchor= W)
        tree.heading("Link", text= "Link", anchor= CENTER)

        cursor.execute("SELECT * FROM CapitalRaise")
        capitalRais = cursor.fetchall()
        print(capitalRais)

        tree.tag_configure('oddrow',background="white")
        tree.tag_configure('evenrow',background="#51B087")

        count_color = 0
        for capital in capitalRais:
            if count_color %2 ==0:
                tree.insert(parent='', index= 'end', iid=capital[0], text="", values=(capital[1],capital[3],capital[2]), tags=('evenrow'))
            else:
                tree.insert(parent='', index= 'end', iid=capital[0], text="", values=(capital[1],capital[3],capital[2]), tags=(''))
    
            count_color +=1
