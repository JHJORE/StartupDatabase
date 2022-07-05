from tkinter import *
from tkinter.ttk import Treeview
import requests


class AidTree(Frame):
    def __init__(self, parent, left_frame, values):
        Frame.__init__(self, parent)


        vertical_scroll = Scrollbar(left_frame)
        vertical_scroll.grid(row=0, column=1, sticky="ns",padx = 0, pady = 20 )

        tree = Treeview(left_frame,height= 10 , yscrollcommand= vertical_scroll.set)
        tree.grid(row = 0, column = 0, sticky = "nswe",padx = 20, pady = 20, ipadx = 20)

        vertical_scroll.config(command = tree.yview)
        tree['column'] = (
        "Sum",
        "GivenBy",
        "Type",
        "Reason",
        "County",
        "DateGiven")

        #colums
        tree.column("#0", width=0, stretch=NO)
        tree.column("Sum", anchor=CENTER, width= 50, )
        tree.column("GivenBy", anchor=W, width= 80, )
        tree.column("Type", anchor=W, width= 80, )
        tree.column("Reason", anchor=W, width= 80, )
        tree.column("County", anchor=W, width= 80, )
        tree.column("DateGiven", anchor=W, width= 80, )
        

        #Headings
        tree.heading("#0", text= "", anchor= W)
        tree.heading("Sum", text= "Sum", anchor= W)
        tree.heading("GivenBy", text= "Given By", anchor= W)
        tree.heading("Type", text= "Type", anchor= CENTER)
        tree.heading("Reason", text= "Reason", anchor= CENTER)
        tree.heading("County", text= "County", anchor= CENTER)
        tree.heading("DateGiven", text= "DateGiven", anchor= CENTER)

        URL = "http://127.0.0.1:8000/Aid/Org/" + str(values[1])
        PARAMS = {"OrgNumber": values[1]}

        response = requests.get(url = URL, params = PARAMS)
        aids = response.json()



        tree.tag_configure('oddrow',background="white")
        tree.tag_configure('evenrow',background="#51B087")

        count_color = 0
        for aid in aids:
            if count_color %2 ==0:
                tree.insert(parent='', index= 'end', iid=aid["AidId"], text="", values=(aid["Sum"],aid["GivenBy"],aid["Type"], aid["Reason"], aid["County"], aid["DateGiven"]), tags=('evenrow'))
            else:
                tree.insert(parent='', index= 'end', iid=aid["AidId"], text="", values=(aid["Sum"],aid["GivenBy"],aid["Type"], aid["Reason"], aid["County"], aid["DateGiven"]), tags=(''))
    
            count_color +=1
