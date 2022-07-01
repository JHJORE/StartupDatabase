from tkinter import*
from tkinter import ttk
import customtkinter
from Components import NavBar, Filter, EditCompany, MainPageTable
import CompanyView
#import Components.NavBar, Components.Filter, Components.EditCompany, Components.MainPageTable
#import Components

class HomePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        


        # #Style
        # style = ttk.Style()
        # style.theme_use("default")
        # style.configure("Treeview",
        # foreground ="black",
        # rowheight = 23,
        # )

        # create frames

        top_frame = customtkinter.CTkFrame(self,
                                height= 60, 
                                corner_radius=0,
                            )
        top_frame.grid(row = 0, column=0, sticky = "nswe")

        filter_frame = customtkinter.CTkFrame(self)
        filter_frame.grid(row = 1, column = 0, sticky = "nswe",padx = 20, pady = 20)

        search_frame = customtkinter.CTkFrame(filter_frame)
        search_frame.grid(row = 0, column = 0, sticky = "nswe",padx = 20, pady = 20)

        tree_frame = customtkinter.CTkFrame(self)
        tree_frame.grid(row = 2, column = 0, sticky = "nswe", padx = 20, pady = 10)

        # bottom_frame = customtkinter.CTkFrame(self)
        # bottom_frame.grid(row = 3, column = 0, sticky = "nswe",padx = 20, pady = 20)


        def open_company(event):
            tree = maintable.get_tree()
            select = tree.focus()
            values = tree.item(select,'values')
            command = lambda : controller.show_frame(CompanyView)

        navbar = NavBar(self, top_frame)

        maintable = MainPageTable(self, tree_frame, open_company())

        filter = Filter(self, search_frame, maintable.get_tree())


        #edit_company_section = EditCompany(self, bottom_frame, maintable.get_tree())

