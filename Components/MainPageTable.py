from tkinter import *
from sql_app import main
from sql_app.database import SessionLocal

class MainPageTable(Frame):
    def __init__(self, parent, tree_frame, tree):
        Frame.__init__(self, parent)
        self.db = SessionLocal()
        #colums
        tree.column("#0", width=0, stretch=NO)
        tree.column("Name", anchor=W, width= 120)
        tree.column("OrgNumber", anchor=W, width= 80)
        tree.column("Email", anchor=CENTER, width= 160)
        tree.column("Sector", anchor=CENTER, width= 180)
        tree.column("Description", anchor=CENTER, width= 120)
        tree.column("Employees", anchor=W, width= 80)
        tree.column("Manicipality", anchor=W, width= 120)

        #Headings
        tree.heading("#0", text= "", anchor= W)
        tree.heading("Name", text= "Name", anchor= W)
        tree.heading("OrgNumber", text= "OrgNumber", anchor= W)
        tree.heading("Email", text= "Email", anchor= CENTER)
        tree.heading("Sector", text= "Sector", anchor= CENTER)
        tree.heading("Description", text= "Description", anchor= CENTER)
        tree.heading("Employees", text= "Employees", anchor= W)
        tree.heading("Manicipality", text= "Manicipality", anchor= W)

        tree.tag_configure('oddrow',background="white")
        tree.tag_configure('evenrow',background="#51B087")

        self.tree = tree

        self.make_treeview()

    def make_treeview(self):
        companies = main.read_companies(db = self.db)
        count_color = 0
        for company in companies:
            if count_color %2 ==0:
                self.tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=('evenrow'))
            else:
                self.tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=(''))
        
            count_color +=1

