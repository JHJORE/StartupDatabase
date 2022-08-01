from cgitb import reset
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import requests
from Components import DeleteBox


class NewFilter(Frame):
    def __init__(self, parent, search_frame, tree, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        search_frame.rowconfigure((10), weight=1)

        self.companyname_entry = customtkinter.CTkEntry(search_frame,
                                placeholder_text="Company Name",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)

        self.companyname_entry.grid(row=0, column=0, padx=10, pady=10)  

        self.sector_entry = customtkinter.CTkEntry(search_frame,
                                placeholder_text="Sector",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)

        self.sector_entry.grid(row=0, column=1, padx=10, pady=10)  
        
        self.municipality_entry = customtkinter.CTkEntry(search_frame,
                                placeholder_text="Municipality",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)

        self.municipality_entry.grid(row=0, column=2, padx=10, pady=10)  

        optionmenu_var = customtkinter.StringVar(value="") 

        self.dropdown_btn = customtkinter.CTkOptionMenu(search_frame, values=["Oppstartstilskudd", "Støtteordning"],width=20,corner_radius =8, variable=optionmenu_var)
        self.dropdown_btn.grid(row=0, column=3, pady=10, padx=10, sticky="ne")

        self.folder_img = ImageTk.PhotoImage(Image.open("./Constants/searchicon.png").resize((20,20),  Image.LANCZOS))
        
        self.search_btn = customtkinter.CTkButton(search_frame, image = self.folder_img,text="", width=20, height= 20, compound= "left", command=self.search_database)
        self.search_btn.grid(row=0, column=4, padx=10, pady=10)

        self.employee_entry1 = customtkinter.CTkEntry(search_frame,
                                    placeholder_text="MinEmployees",
                                width=180,
                                height=25,
                                border_width=2,
                                corner_radius=5)
        self.employee_entry1.grid(row=1, column=0, padx=10, pady=10)
    
        self.employee_entry2 = customtkinter.CTkEntry(search_frame,
                                    placeholder_text="MaxEmployees",
                                width=180,
                                height=25,
                                border_width=2,
                                corner_radius=5)
        self.employee_entry2.grid(row=1, column=1, padx=10, pady=10)

        delete_btn = customtkinter.CTkButton(search_frame, text="Delete Company", command= self.openDelteBox)
        delete_btn.grid(row=1, column=2, columnspan=1, pady=10, padx=10, ipadx= 30, sticky="ne")

        clearn_btn = customtkinter.CTkButton(search_frame, text="clear",width=20, command= self.clear)
        clearn_btn.grid(row=1, column=3, pady=10, padx=10, sticky="ne")

        self.tree = tree

    def search_database(self):
        CompanyName = self.companyname_entry.get()
        Sector = self.sector_entry.get()
        EmployeesMin = 0 if self.employee_entry1.get() == "" else self.employee_entry1.get()
        EmployeesMax = 1000000 if self.employee_entry2.get() == "" else self.employee_entry2.get()
        Municipality = self.municipality_entry.get()
        Aidtype = self.dropdown_btn.get()


        URL = "http://127.0.0.1:8000/Company/"
        # sett inn i PARAMS når det går: "CompanyName": CompanyName,
        PARAMS = {"CompanyName": CompanyName, "Sector": Sector, "EmployeesMin": EmployeesMin, "EmployeesMax": EmployeesMax, "Municipality": Municipality, "Type": Aidtype}

        r = requests.get(url = URL, params = PARAMS)
        companies = r.json()
        self.make_treeview(companies)

        

    def clear(self):
        self.employee_entry1.delete(0, END)
        self.employee_entry2.delete(0, END)
        self.municipality_entry.delete(0, END)
        self.sector_entry.delete(0, END)
        self.companyname_entry.delete(0, END)
        self.dropdown_btn.set("")
   


    def make_treeview(self, companies):
        for company in self.tree.get_children():
                self.tree.delete(company)
        count_color = 0
        for company in companies:
            if count_color %2 ==0:
                self.tree.insert(parent='', index= 'end', iid=company["OrgNumber"], text="", values=(company["CompanyName"],company["OrgNumber"],company["Email"],company["Sector"],company["Description"],company["Employees"],company["Municipality"]), tags=('evenrow'))
            else:
                self.tree.insert(parent='', index= 'end', iid=company["OrgNumber"], text="", values=(company["CompanyName"],company["OrgNumber"],company["Email"],company["Sector"],company["Description"],company["Employees"],company["Municipality"]), tags=(''))
            count_color +=1

    def openDelteBox(self):
        company = self.tree.focus()
        row = self.tree.item(company)
        values = row.get('values')

        if(values != ""):
            DeleteBox.DeleteBox(self.parent,values,self.tree)
    
