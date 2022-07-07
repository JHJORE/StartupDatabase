from tkinter import *
from tkinter.ttk import Treeview
import requests
from DataGathering import CapitalRaises

class CapitalTree(Frame):
    def __init__(self, parent, right_frame, values):
        Frame.__init__(self, parent)
        self.values = values


        vertical_scroll = Scrollbar(right_frame)
        vertical_scroll.grid(row=0, column=1, sticky="ns",padx = 0, pady = 20 )

        self.tree = Treeview(right_frame,height= 4 , yscrollcommand= vertical_scroll.set)
        self.tree.grid(row = 0, column = 0, sticky = "nswe",padx = 20, pady = 20, ipadx = 10)

        vertical_scroll.config(command = self.tree.yview)
        self.tree['column'] = (
        "Sum",
        "Date",
        "Link")

        #colums
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Sum", anchor=CENTER, width= 80, stretch= 20)
        self.tree.column("Date", anchor=W, width= 80, stretch= 20)
        self.tree.column("Link", anchor=W, width= 500, stretch= 20)

        #Headings
        self.tree.heading("#0", text= "", anchor= W)
        self.tree.heading("Sum", text= "Sum", anchor= W)
        self.tree.heading("Date", text= "Date", anchor= W)
        self.tree.heading("Link", text= "Link", anchor= CENTER)

        self.tree.tag_configure('oddrow',background="white")
        self.tree.tag_configure('evenrow',background="#51B087")

        URL = "http://127.0.0.1:8000/CapitalRaise/Org/" + str(values[1])
        PARAMS = {"OrgNumber": values[1]}
        response = requests.get(url = URL, params = PARAMS)
        capitalraises = response.json()

        if len(capitalraises) == 0:
            CapitalRaises.capital_raises_to_db(values[1])
            response = requests.get(url = URL, params = PARAMS)
            capitalraises = response.json()
             

        count_color = 0
        for capitalraise in capitalraises:
            if count_color %2 ==0:
                self.tree.insert(parent='', index= 'end', iid=capitalraise["RaiseId"], text="", values=(capitalraise["Sum"],capitalraise["Date"],capitalraise["Link"]), tags=('evenrow'))
            else:
                self.tree.insert(parent='', index= 'end', iid=capitalraise["RaiseId"], text="", values=(capitalraise["Sum"],capitalraise["Date"],capitalraise["Link"]), tags=(''))
    
            count_color +=1

    def get_tree(self):
        return self.tree
