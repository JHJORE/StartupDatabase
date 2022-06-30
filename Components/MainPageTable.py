from tkinter import *
from tkinter import ttk
from sql_app import main
from sql_app.database import SessionLocal

class MainPageTable(Frame):
    def __init__(self, parent, tree_frame, open_company):
        Frame.__init__(self, parent)
        self.db = SessionLocal()

        vertical_scroll = Scrollbar(tree_frame)
        vertical_scroll.pack(side=RIGHT, fill = Y )

        self.tree = ttk.Treeview(tree_frame, yscrollcommand= vertical_scroll.set)
        self.tree.pack()
        vertical_scroll.config(command = self.tree.yview)

        self.tree['column'] = (
        "Name",
        "OrgNumber",
        "Email",
        "Sector",
        "Description",
        "Employees",
        "Municipality")
        #colums
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Name", anchor=W, width= 120)
        self.tree.column("OrgNumber", anchor=W, width= 80)
        self.tree.column("Email", anchor=CENTER, width= 160)
        self.tree.column("Sector", anchor=CENTER, width= 180)
        self.tree.column("Description", anchor=CENTER, width= 120)
        self.tree.column("Employees", anchor=W, width= 80)
        self.tree.column("Municipality", anchor=W, width= 120)

        #Headings
        self.tree.heading("#0", text= "", anchor= W)
        self.tree.heading("Name", text= "Name", anchor= W)
        self.tree.heading("OrgNumber", text= "OrgNumber", anchor= W)
        self.tree.heading("Email", text= "Email", anchor= CENTER)
        self.tree.heading("Sector", text= "Sector", anchor= CENTER)
        self.tree.heading("Description", text= "Description", anchor= CENTER)
        self.tree.heading("Employees", text= "Employees", anchor= W)
        self.tree.heading("Municipality", text= "Municipality", anchor= W)

        self.tree.tag_configure('oddrow',background="white")
        self.tree.tag_configure('evenrow',background="#51B087")

        self.make_treeview()
        self.tree.bind("<Double-1>", open_company)

    def get_tree(self):
        return self.tree

    def make_treeview(self):
        companies = main.read_companies(db = self.db)
        count_color = 0
        for company in companies:
            if count_color %2 ==0:
                self.tree.insert(parent='', index= 'end', iid=company.OrgNumber, text="", values=(company.CompanyName,company.OrgNumber,company.Email,company.Sector,company.Description,company.Employees,company.Municipality), tags=('evenrow'))
            else:
                self.tree.insert(parent='', index= 'end', iid=company.OrgNumber, text="", values=(company.CompanyName,company.OrgNumber,company.Email,company.Sector,company.Description,company.Employees,company.Municipality), tags=(''))
        
            count_color +=1


