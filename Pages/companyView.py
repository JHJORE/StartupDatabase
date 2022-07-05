from tkinter import*
import customtkinter
from Components import AidTree, CapitalTree, EditCompany, NavBar

class CompanyView(Frame):

    def __init__(self, parent, controller, values):
        Frame.__init__(self, parent)
        self.values = values
        self.parent = parent

        #Frames
        top_frame = customtkinter.CTkFrame(self,
                                height= 200, 
                                corner_radius=0,
                            )
        top_frame.grid(row = 0, column = 0, sticky = "nswe")
        
        middle_frame = customtkinter.CTkFrame(self)
        middle_frame.grid(row = 1, column = 0,  columnspan=2, sticky = "nswe", padx = 10, pady = 10)

        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row = 2, column = 0, sticky = "nswe", padx = 20, pady = 10)

        right_frame = customtkinter.CTkFrame(self)
        right_frame.grid(row = 2, column = 1, sticky = "nswe", padx = 20, pady = 10)

        #Components
        navbar = NavBar.NavBar(parent, controller, top_frame)
        editcompany = EditCompany.EditCompany(self, middle_frame, self.values, controller)
        capitaltree = CapitalTree.CapitalTree(self, right_frame, values)
        aid = AidTree.AidTree(self,left_frame, values)
