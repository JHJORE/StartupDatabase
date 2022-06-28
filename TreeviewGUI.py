

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

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title('Startup Database')
root.geometry("920x700")
conn = sqlite3.connect('sql_app.db')
cursor = conn.cursor()
#Style
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
foreground ="black",
rowheight = 23,
)

# create tree frames

frame_top = customtkinter.CTkFrame(root,
                        height= 60, 
                        corner_radius=0,
                        padx = 0,
                        pady = 0)
frame_top.grid(row = 0, column=0, sticky = "nswe")


tree_frame = customtkinter.CTkFrame(root)
tree_frame.grid(row = 1, column = 0, sticky = "nswe", padx = 20, pady = 10)

frame_bottom = customtkinter.CTkFrame(root)
frame_bottom.grid(row = 2, column = 0, sticky = "nswe",padx = 20, pady = 20)

vertical_scroll = Scrollbar(tree_frame)
vertical_scroll.pack(side=RIGHT, fill = Y )

tree = ttk.Treeview(tree_frame, yscrollcommand= vertical_scroll.set)
tree.pack()

vertical_scroll.config(command = tree.yview)

# img = ImageTk.PhotoImage(Image.open("fi-og-img.png").resize(20,20))

# img_lable = customtkinter.CTkLabel(frame_top, image = img)
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
    

    return models.Company(
        OrgNumber = values[1],
        CompanyName = values[0],
        Description = values[3],
     
        
    )


def update_company():

    
    
    conn = sqlite3.connect('sql_app.db')
    cursor = conn.cursor()
    OrgNumber = tree.focus

    main.update_Company(db=db, OrgNumber = OrgNumber, Company= create_company())

    conn.commit()
    conn.close()
    

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
    print(values)


    values = tree.item(select,'values')

    name_entry.insert(0,values[2])
    email_entry.insert(0, values[0])
    sector_edit.insert(0, values[-1])
    
    

def clicked(event):
    selected()
   


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
tree.tag_configure('evenrow',background="lightblue")

global count_color
count_color = 0
for company in companies:
    if count_color %2 ==0:
        tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3]), tags=('evenrow'))
    else:
        tree.insert(parent='', index= 'end', iid=company[0], text="", values=(company[1],company[0],company[2],company[3]), tags=(''))
    
    count_color +=1



folder_img = ImageTk.PhotoImage(Image.open("fi-og-img.png").resize((70,70),  Image.LANCZOS))
icon = customtkinter.CTkButton(frame_top, image = folder_img,text="",borderwidth=0, width=70, height= 70, compound= "left" )
icon.grid(row=0, column=0, padx=20, pady=10)

folder_img = ImageTk.PhotoImage(Image.open("database.png").resize((40,40),  Image.LANCZOS))
database_btn = customtkinter.CTkButton(frame_top, image = folder_img,text="", width=50, height= 50, compound= "left" )
database_btn.grid(row=0, column=1, padx=20, )

folder_img = ImageTk.PhotoImage(Image.open("company.png").resize((40,40),  Image.LANCZOS))
company_btn = customtkinter.CTkButton(frame_top, image = folder_img,text="", width=50, height= 50, compound= "left" )
company_btn.grid(row=0, column=3, padx=20, pady=10)

folder_img = ImageTk.PhotoImage(Image.open("list.png").resize((40,40),  Image.LANCZOS))
list_btn = customtkinter.CTkButton(frame_top, image = folder_img,text="", width=50, height= 50, compound= "left" )
list_btn.grid(row=0, column=4, padx=20, pady=10)




email_entry = customtkinter.CTkEntry(frame_bottom,
                                placeholder_text="Comany Email",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)
email_entry.grid(row=0, column=5,padx=10, pady=10)

# company_name = customtkinter.CTkLabel(frame_bottom, text="Name", width=180,height=25, corner_radius=8)
# company_name.grid(row=0, column= 0,  padx=10, pady=10)

name_entry = customtkinter.CTkEntry(frame_bottom,
                                placeholder_text="Company Name",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)
name_entry.grid(row=0, column=0, padx=10, pady=10)




sector_edit = customtkinter.CTkEntry(frame_bottom,
                                placeholder_text="Sector",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=5)
sector_edit.grid(row=0, column=7,padx=10, pady=10)


# edit_email = Label(frame_bottom, text="Email")
# edit_email.grid(row=0, column= 3)


# edit_Sector = Label(frame_bottom, text="Sector")
# edit_Sector.grid(row=0, column= 5)

update_btn = customtkinter.CTkButton(frame_bottom, text = 'Save Changes', command=update_company)
update_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx= 30 )

remove_company_btn = customtkinter.CTkButton(frame_bottom, text="Remove Company", command= remove_company)
remove_company_btn.grid(row=6, column=4, columnspan=2, pady=10, padx=10, ipadx= 30 )


excel_btn = customtkinter.CTkButton(frame_bottom, text="Export to Excel", command= remove_company)
excel_btn.grid(row=6, column=6, columnspan=2, pady=10, padx=10, ipadx= 30 )


tree.bind("<ButtonRelease-1>", clicked)



root.mainloop()
