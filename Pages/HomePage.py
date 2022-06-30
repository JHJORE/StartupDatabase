from tkinter import*
from tkinter import ttk
import customtkinter

# import os
# import sys

# script_dir = os.path.dirname( __file__ )
# mymodule_dir = os.path.join( script_dir, '..', 'Components' )
# sys.path.append( mymodule_dir )
# import NavBar, MainPageTable, Filter, EditCompany

from Components import NavBar, Filter, EditCompany, MainPageTable
#import Components.NavBar, Components.Filter, Components.EditCompany, Components.MainPageTable
#import Components

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
WIDTH = 920
HEIGHT = 700


root = customtkinter.CTk()
root.title('Startup Database')
root.geometry(f"{WIDTH}x{HEIGHT}")

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


def clicked(event):
    tree = maintable.get_tree()
    select = tree.focus()
    values = tree.item(select,'values')
    edit_company_section.selected(values=values)

navbar = NavBar(root, top_frame)

maintable = MainPageTable(root, tree_frame, clicked)

filter = Filter(root, search_frame, maintable.get_tree())

edit_company_section = EditCompany(root, bottom_frame, maintable.get_tree())




root.mainloop()
