from tkinter import *
from tkinter.ttk import Treeview
import sqlite3


class AidTree(Frame):
    def __init__(self, parent, left_frame, values):
        Frame.__init__(self, parent)
        conn = sqlite3.connect('sql_app.db')
        cursor = conn.cursor()


        vertical_scroll = Scrollbar(left_frame)
        vertical_scroll.grid(row=0, column=1, sticky="ns",padx = 0, pady = 20 )

        tree = Treeview(left_frame,height= 4 , yscrollcommand= vertical_scroll.set)
        tree.grid(row = 0, column = 0, sticky = "nswe",padx = 12, pady = 12, ipadx = 12)

        vertical_scroll.config(command = tree.yview)
        tree['column'] = (
        "Sum",
        "GivenBy",
        "Type",
        "Reason",
        "Country",
        "DateGiven")

        #colums
        tree.column("#0", width=0, stretch=NO)
        tree.column("Sum", anchor=CENTER, width= 50, )
        tree.column("GivenBy", anchor=W, width= 80, )
        tree.column("Type", anchor=W, width= 300, )
        tree.column("Reason", anchor=W, width= 220, )
        tree.column("Country", anchor=W, width= 80, )
        tree.column("DateGiven", anchor=W, width= 80, )
        

        #Headings
        tree.heading("#0", text= "", anchor= W)
        tree.heading("Sum", text= "Sum", anchor= W)
        tree.heading("GivenBy", text= "Given By", anchor= W)
        tree.heading("Type", text= "Type", anchor= CENTER)
        tree.heading("Reason", text= "Reason", anchor= CENTER)
        tree.heading("Country", text= "Country", anchor= CENTER)
        tree.heading("DateGiven", text= "DateGiven", anchor= CENTER)

        cursor.execute("SELECT *, oid FROM Aid WHERE OrgNumber = ?", (values[1],))
        capitalRais = cursor.fetchall()

        tree.tag_configure('oddrow',background="white")
        tree.tag_configure('evenrow',background="#51B087")

        count_color = 0
        for capital in capitalRais:
            if count_color %2 ==0:
                tree.insert(parent='', index= 'end', iid=capital[0], text="", values=(capital[1],capital[3],capital[2]), tags=('evenrow'))
            else:
                tree.insert(parent='', index= 'end', iid=capital[0], text="", values=(capital[1],capital[3],capital[2]), tags=(''))
    
            count_color +=1
        conn.commit()
        conn.close()
