from audioop import add
from itertools import count
from tkinter import*
from tkinter import ttk

from sql_app import main,models
import sqlite3
from turtle import right, update

from soupsieve import select

root = Tk()
root.title('Startup Database')
root.geometry("1000x400")
conn = sqlite3.connect('sql_app.db')
cursor = conn.cursor()
#Style
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
foreground ="black",
rowheight = 23,
)


tree_frame = Frame(root)
tree_frame.pack(pady=20)

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






def create_company():
    orgNumber = str(tree.focus)
    row = tree.item(orgNumber)
    company = models.Company(
        
    )


def update_company():

    
    
    conn = sqlite3.connect('sql_app.db')
    cursor = conn.cursor()
    

    



    cursor.execute("""UPDATE Company SET 
        CompanyName = :companyname,
        Email = :email,
        Sector = :sector
        WHERE OrgNumber = :orgNumber""",
        {
            'companyname':name_edit.get(), 
            'email' : email_edit.get(),
            'sector': sector_edit.get(),
            'orgNumber': orgNumber
        })

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
    email_edit.delete(0,END) 
    sector_edit.delete(0,END)
    name_edit.delete(0,END)

    select = tree.focus()
    values = tree.item(select,'values')

    email_edit.insert(0, values[3])
    sector_edit.insert(0, values[2])
    name_edit.insert(0,values[1])
    

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






fram_add = Frame(root)
fram_add.pack(pady = 20)

email_edit = Entry(fram_add, width=30)
email_edit.grid(row=0, column=1)

name_edit = Entry(fram_add, width=30)
name_edit.grid(row=0, column=4)

sector_edit = Entry(fram_add, width=30)
sector_edit.grid(row=0, column=6)


edit_email = Label(fram_add, text="Email")
edit_email.grid(row=0, column= 0)

edit_Name = Label(fram_add, text="Name")
edit_Name.grid(row=0, column= 3)

edit_Sector = Label(fram_add, text="Sector")
edit_Sector.grid(row=0, column= 5)
remove_company_btn = Button(fram_add, text="Remove Company", command= remove_company)
remove_company_btn.grid(row=6, column=4, columnspan=2, pady=10, padx=10, ipadx= 45 )


update_btn = Button(fram_add, text = 'Save Changes', command=update_company)
update_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx= 45 )


tree.bind("<ButtonRelease-1>", clicked)



root.mainloop()
