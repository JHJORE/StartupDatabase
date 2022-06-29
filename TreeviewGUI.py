

from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter
from matplotlib import image

from sqlalchemy import column, values

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


# img = ImageTk.PhotoImage(Image.open("fi-og-img.png").resize(20,20))

# img_lable = customtkinter.CTkLabel(top_frame, image = img)
# img_lable.grid(row=0, column=0, padx=10, pady=10)

tree['column'] = (
    "Name",
    "OrgNumber",
    "Email",
    "Sector",
    "Description",
    "Employees",
    "Manicipality")





def create_company():
    select = tree.focus()
    row = tree.item(select)
    values = row.get('values')
    
    print(values[1])
    print(values[0])
    print(values[-1])

    return models.Company(
        OrgNumber = values[1],
        CompanyName = values[0],
        Description = values[-1],   
    )


def update_company():

    
    
    select = tree.focus()
    row = tree.item(select)
    values = row.get('values')
    OrgNumber = values[1]

    main.update_Company(db=db, OrgNumber = OrgNumber, Company= create_company())

    
    

def remove_company():
    conn = sqlite3.connect('sql_app.db')
    cursor = conn.cursor()

    companies = tree.selection()
    for company in companies:
        orgNumber = company
        print(company)
        cursor.execute("DELETE FROM Company WHERE OrgNumber = "+ orgNumber)
        tree.delete(company)

    conn.commit()
    conn.close()

def selected():
    email_entry.delete(0,END) 
    sector_edit.delete(0,END)
    name_entry.delete(0,END)

    select = tree.focus()
    row = tree.item(select)
    values = row.get('values')
    


    values = tree.item(select,'values')

    name_entry.insert(0,values[0])
    email_entry.insert(0, values[2])
    sector_edit.insert(0, values[-1])
    
    

def clicked(event):
    selected()


def make_treeview(companies):
    count_color = 0
    for company in companies:
        if count_color %2 ==0:
            tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=('evenrow'))
        else:
            tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3],company[4],company[5],company[6]), tags=(''))
    
        count_color +=1

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


def switchmode():
    state = mode_switch.get()
    if(state == "on"):
        customtkinter.set_appearance_mode("Dark")
    else:
        customtkinter.set_appearance_mode("System")



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

cursor.execute("SELECT *, oid FROM Company ")
companies = cursor.fetchall()

tree.tag_configure('oddrow',background="white")
tree.tag_configure('evenrow',background="#51B087")


make_treeview(companies)



folder_img = ImageTk.PhotoImage(Image.open("fi-og-img.png").resize((70,70),  Image.LANCZOS))
icon = customtkinter.CTkButton(top_frame, image = folder_img,text="",borderwidth=0, width=70, height= 70, compound= "left" )
icon.grid(row=0, column=0, padx=20, pady=10)

folder_img = ImageTk.PhotoImage(Image.open("database.png").resize((40,40),  Image.LANCZOS))
database_btn = customtkinter.CTkButton(top_frame, image = folder_img,text="", width=50, height= 50, compound= "left" )
database_btn.grid(row=0, column=1, padx=10, )

folder_img = ImageTk.PhotoImage(Image.open("company.png").resize((40,40),  Image.LANCZOS))
company_btn = customtkinter.CTkButton(top_frame, image = folder_img,text="", width=50, height= 50, compound= "left" )
company_btn.grid(row=0, column=2, padx=20, pady=10)

folder_img = ImageTk.PhotoImage(Image.open("list.png").resize((40,40),  Image.LANCZOS))

list_btn = customtkinter.CTkButton(top_frame, image = folder_img,text="", width=50, height= 50, compound= "left" )
list_btn.grid(row=0, column=3, padx=20, pady=10)












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

mode_switch = customtkinter.CTkSwitch(top_frame, text = "Dark Mode", command= switchmode, onvalue= "on", offvalue= "off")
mode_switch.grid(row=0, column=9, padx=10, pady=10)


sector_edit = customtkinter.CTkEntry(bottom_frame,
                                placeholder_text="Sector",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)
sector_edit.grid(row=1, column=1,padx=10, pady=10)




# edit_email = Label(bottom_frame, text="Email")
# edit_email.grid(row=0, column= 3)


# edit_Sector = Label(bottom_frame, text="Sector")
# edit_Sector.grid(row=0, column= 5)

update_btn = customtkinter.CTkButton(bottom_frame, text = 'Save Changes', command=update_company)
update_btn.grid(row=3, column=0, columnspan=1, pady=10, padx=10, ipadx= 30 )

notes_btn = customtkinter.CTkButton(bottom_frame, text="Notes", command= remove_company)
notes_btn.grid(row=3, column=1, columnspan=1, pady=10, padx=10, ipadx= 30 )

news_btn = customtkinter.CTkButton(bottom_frame, text="News Articles", command= remove_company)
news_btn.grid(row=3, column=2, columnspan=1, pady=10, padx=10, ipadx= 30 )

excel_btn = customtkinter.CTkButton(bottom_frame, text="Export to Excel", command= remove_company)
excel_btn.grid(row=3, column=3, columnspan=1, pady=10, padx=10, ipadx= 30 )






tree.bind("<ButtonRelease-1>", clicked)



root.mainloop()
