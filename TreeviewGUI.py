

from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter
from matplotlib import image
from Components import NavBar

from sqlalchemy import column, values
from Components.EditCompany import EditCompany
from Components.MainPageTable import MainPageTable

from sql_app import main,models
import sqlite3
from sql_app import database

from sql_app.database import SessionLocal
db = SessionLocal()

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
WIDTH = 920
HEIGHT = 700


root = customtkinter.CTk()
root.title('Startup Database')
root.geometry(f"{WIDTH}x{HEIGHT}")
conn = sqlite3.connect('sql_app.db')
cursor = conn.cursor()

root.columnconfigure((0), weight=1)
root.rowconfigure((1,2,3,4,5,6,7,8,9), weight=1)


#Style
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
foreground ="black",
rowheight = 23,
)

# create frames

top_frame = customtkinter.CTkFrame(root,
                        height= 60, 
                        corner_radius=0,
                    )
top_frame.grid(row = 0, column=0, sticky = "nswe")






filter_frame = customtkinter.CTkFrame(root)
filter_frame.grid(row = 1, column = 0, sticky = "nswe",padx = 20, pady = 20)



search_frame = customtkinter.CTkFrame(filter_frame)
search_frame.grid(row = 0, column = 0, sticky = "nswe",padx = 20, pady = 20)

tree_frame = customtkinter.CTkFrame(root)
tree_frame.grid(row = 2, column = 0, sticky = "nswe", padx = 20, pady = 10)

bottom_frame = customtkinter.CTkFrame(root)
bottom_frame.grid(row = 3, column = 0, sticky = "nswe",padx = 20, pady = 20)

vertical_scroll = Scrollbar(tree_frame)
vertical_scroll.pack(side=RIGHT, fill = Y )

tree = ttk.Treeview(tree_frame, yscrollcommand= vertical_scroll.set)
tree.pack()

vertical_scroll.config(command = tree.yview)


tree['column'] = (
    "Name",
    "OrgNumber",
    "Email",
    "Sector",
    "Description",
    "Employees",
    "Manicipality")
    
    




# def make_treeview(companies):
#     count_color = 0
#     for company in companies:
#         if count_color %2 ==0:
#             tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=('evenrow'))
#         else:
#             tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=(''))
    
#         count_color +=1

def employee_treeview(companies):
    count_color = 0
    employees_start = int(employee_entry1.get())
    employees_end = int(employee_entry2.get())
    for company in companies:
        employed = int(company[5])
        if(employees_end>= employed and employed>=employees_start):
            if count_color %2 ==0:
                tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=('evenrow'))
            else:
                tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=(''))
    
            count_color +=1
   
def search_database():
    conn = sqlite3.connect('sql_app.db')
    cursor = conn.cursor()
    filter = search_dropdown.get()
    company_search = search_entry.get()
    cursor.execute("SELECT *, oid FROM Company ")
    companies = cursor.fetchall()
    if(company_search != ""): 
        for company in tree.get_children():
            tree.delete(company)
        cursor.execute(f"SELECT *, oid FROM Company WHERE {filter} like ?", (company_search,))
        companies = cursor.fetchall()
        make_treeview(companies)
        print("filter")
    else:
        for company in tree.get_children():
            tree.delete(company)
        if(filter == "Employees"): #trenges ettersom vi sorterer i tall og ikke items
            employee_treeview(companies)
            print("success")
        else:
            make_treeview(companies) 
        print("normal")  
    conn.commit()
    conn.close()

def check_dropdown(self):
    selected = search_dropdown.get()
    if(selected == "Employees"):
        employee_entry1.grid(row=0, column=2, padx=10, pady=10)
        employee_entry2.grid(row=0, column=3, padx=10, pady=10)
    else:
        employee_entry1.grid_remove()
        employee_entry2.grid_remove()



# #colums
# tree.column("#0", width=0, stretch=NO)
# tree.column("Name", anchor=W, width= 120)
# tree.column("OrgNumber", anchor=W, width= 80)
# tree.column("Email", anchor=CENTER, width= 160)
# tree.column("Sector", anchor=CENTER, width= 180)
# tree.column("Description", anchor=CENTER, width= 120)
# tree.column("Employees", anchor=W, width= 80)
# tree.column("Manicipality", anchor=W, width= 120)

# #Headings
# tree.heading("#0", text= "", anchor= W)
# tree.heading("Name", text= "Name", anchor= W)
# tree.heading("OrgNumber", text= "OrgNumber", anchor= W)
# tree.heading("Email", text= "Email", anchor= CENTER)
# tree.heading("Sector", text= "Sector", anchor= CENTER)
# tree.heading("Description", text= "Description", anchor= CENTER)
# tree.heading("Employees", text= "Employees", anchor= W)
# tree.heading("Manicipality", text= "Manicipality", anchor= W)

# cursor.execute("SELECT *, oid FROM Company ")
# companies = cursor.fetchall()

# tree.tag_configure('oddrow',background="white")
# tree.tag_configure('evenrow',background="#51B087")


# make_treeview(companies)


navbar = NavBar.NavBar(root, top_frame)

maintable = MainPageTable.MainPageTable(root, tree_frame)

edit_company_section = EditCompany(root, bottom_frame, tree)

search_entry = customtkinter.CTkEntry(search_frame,
                                placeholder_text="Search Company",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)

search_entry.grid(row=0, column=0, padx=10, pady=10)  


folder_img = ImageTk.PhotoImage(Image.open("searchicon.png").resize((20,20),  Image.LANCZOS))
search_button = customtkinter.CTkButton(search_frame, image = folder_img,text="", width=20, height= 20, compound= "left", command=search_database )
search_button.grid(row=0, column=5, padx=10, pady=10)
search_dropdown = customtkinter.CTkOptionMenu(search_frame,
                                                values=["CompanyName",
                                                "OrgNumber", 
                                                "Sector", 
                                                "Employees", 
                                                "Municipality"],
                                                command=check_dropdown
                                            )
search_dropdown.grid(row=0, column=1, padx=10, pady=10)

employee_entry1 = customtkinter.CTkEntry(search_frame,
                                placeholder_text="Start",
                               width=60,
                               height=25,
                               border_width=2,
                               corner_radius=5)
employee_entry2 = customtkinter.CTkEntry(search_frame,
                                placeholder_text="End",
                               width=60,
                               height=25,
                               border_width=2,
                               corner_radius=5)




# excel_btn = customtkinter.CTkButton(bottom_frame, text="Export to Excel", command= remove_company)
# excel_btn.grid(row=6, column=6, columnspan=2, pady=10, padx=10, ipadx= 30 )

def clicked(event):
    edit_company_section.selected()


tree.bind("<ButtonRelease-1>", clicked)



root.mainloop()
