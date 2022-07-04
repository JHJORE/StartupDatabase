from tkinter import*
from tkinter import ttk
import customtkinter

from Components import NavBar, Filter, EditCompany, MainPageTable, NewFilter
import CompanyView


class HomePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        

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


        def open_company(event):
            tree = maintable.get_tree()
            select = tree.focus()
            values = tree.item(select,'values')
            new_frame = CompanyView.CompanyView(parent, controller, values)
            controller.show_frame(new_frame) 

        navbar = NavBar.NavBar(self, controller, top_frame)

        maintable = MainPageTable(self, tree_frame, open_company)

        filter = NewFilter(self, search_frame, maintable.get_tree())

