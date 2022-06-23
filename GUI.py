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

def delete_company():
    conn = sqlite3.connect('sql_app.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Company WHERE OrgNumber = "+ delete_box.get())
    


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

conn.commit()
conn.close()
root.mainloop()
