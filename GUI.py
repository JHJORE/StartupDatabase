from ast import Global
import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import sqlite3 as sql

root = Tk()
root.title('Startup Database')
root.geometry("400x400")

# logo = Image.open('fi-og-img.png')
# logo.save('fi-og-img.png', format= 'ICO')

# root.iconbitmap(logo)
# label = Label(root, text = 'database')

# logo = Image.open('fi-og-img.png')

# # folkebilder = ImageTk.PhotoImage(Image.open('fi-og-img.png'))



conn = sqlite3.connect('sql_app.db')
cursor = conn.cursor()



def query():
    conn = sqlite3.connect('sql_app.db')
    cursor = conn.cursor()

    cursor.execute("SELECT *, oid FROM Company ")
    companies = cursor.fetchall()
    print(companies)
    print_company = ''
    for company in companies:
        print_company += str(str(company) + "\n")


    query_label = Label(root, text = print_company)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()
    
    

def save_changes():
    conn = sqlite3.connect('sql_app.db')
    cursor = conn.cursor()

    orgNumber = delete_box.get()

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
    edit.destroy()


def delete_company():
    conn = sqlite3.connect('sql_app.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Company WHERE OrgNumber = "+ delete_box.get())
    


    conn.commit()
    conn.close()


def edit_company():
    global edit
    edit = Tk()
    edit.title('Edit Company')
    edit.geometry("400x300")

    conn = sqlite3.connect('sql_app.db')
    cursor = conn.cursor()
    orgNumber = delete_box.get()
    cursor.execute("SELECT * FROM Company WHERE OrgNumber ="+ orgNumber)
    companies = cursor.fetchall()

    global email_edit
    global name_edit
    global sector_edit
    

    email_edit = Entry(edit, width=30)
    email_edit.grid(row=0, column=1)

    name_edit = Entry(edit, width=30)
    name_edit.grid(row=1, column=1)

    sector_edit = Entry(edit, width=30)
    sector_edit.grid(row=2, column=1)


    edit_email = Label(edit, text="Email")
    edit_email.grid(row=0, column= 0)

    edit_Name = Label(edit, text="Name")
    edit_Name.grid(row=1, column= 0)

    edit_Sector = Label(edit, text="Sector")
    edit_Sector.grid(row=2, column= 0)


    save_btn = Button(edit, text = 'Save Changes', command=save_changes)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx= 145 )

    print(companies)

    for company in companies:
        name_edit.insert(0,company[1])
        email_edit.insert(0,company[2])
        sector_edit.insert(0,company[3])

    conn.commit()
    conn.close()


delete_box_label = Label(root, text="Delete Company(OrgNumber)")
delete_box_label.grid(row=9, column= 0)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

query_btn = Button(root, text = 'Show Companies', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx= 137 )

delete_btn = Button(root, text = "Delete Company", command= delete_company)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx= 135)

edit_btn = Button(root, text = "Edit Company", command= edit_company)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx= 135)

conn.commit()
conn.close()
root.mainloop()
