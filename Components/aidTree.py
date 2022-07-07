from tkinter import *
from tkinter.ttk import Treeview
import requests


class AidTree(Frame):
    def __init__(self, parent, left_frame, values):
        Frame.__init__(self, parent)


        vertical_scroll = Scrollbar(left_frame)
        vertical_scroll.grid(row=0, column=1, sticky="ns",padx = 0, pady = 20 )

        self.tree = Treeview(left_frame,height= 4 , yscrollcommand= vertical_scroll.set)
        self.tree.grid(row = 0, column = 0, sticky = "nswe",padx = 12, pady = 12, ipadx = 12)

        vertical_scroll.config(command = self.tree.yview)
        self.tree['column'] = (
        "Sum",
        "GivenBy",
        "Type",
        "Reason",
        "County",
        "DateGiven")

        #colums
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Sum", anchor=CENTER, width= 50, )
        self.tree.column("GivenBy", anchor=W, width= 80, )
        self.tree.column("Type", anchor=W, width= 220, )
        self.tree.column("Reason", anchor=W, width= 300, )
        self.tree.column("County", anchor=W, width= 80, )
        self.tree.column("DateGiven", anchor=W, width= 80, )
        

        #Headings
        self.tree.heading("#0", text= "", anchor= W)
        self.tree.heading("Sum", text= "Sum", anchor= W)
        self.tree.heading("GivenBy", text= "Given By", anchor= W)
        self.tree.heading("Type", text= "Type", anchor= CENTER)
        self.tree.heading("Reason", text= "Reason", anchor= CENTER)
        self.tree.heading("County", text= "County", anchor= CENTER)
        self.tree.heading("DateGiven", text= "DateGiven", anchor= CENTER)

        URL = "http://127.0.0.1:8000/Aid/Org/" + str(values[1])
        PARAMS = {"OrgNumber": values[1]}

        response = requests.get(url = URL, params = PARAMS)
        aids = response.json()



        self.tree.tag_configure('oddrow',background="white")
        self.tree.tag_configure('evenrow',background="#51B087")

        count_color = 0
        for aid in aids:
            if count_color %2 ==0:
                self.tree.insert(parent='', index= 'end', iid=aid["AidId"], text="", values=(aid["Sum"],aid["GivenBy"],aid["Type"], aid["Reason"], aid["County"], aid["DateGiven"]), tags=('evenrow'))
            else:
                self.tree.insert(parent='', index= 'end', iid=aid["AidId"], text="", values=(aid["Sum"],aid["GivenBy"],aid["Type"], aid["Reason"], aid["County"], aid["DateGiven"]), tags=(''))
    
            count_color +=1

    def get_tree(self):
        return self.tree
