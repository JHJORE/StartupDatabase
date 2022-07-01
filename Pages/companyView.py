from tkinter import*
from tkinter import ttk
import customtkinter
import sqlite3
from Components import AidTree, CapitalTree, EditCompany

class CompanyView(Frame):

    def __init__(self, parent, values):
        Frame.__init__(self, parent)
        self.values = values

        #Frames
        top_frame = customtkinter.CTkFrame(self)
        top_frame.grid(row = 0, column = 0,  columnspan=2, sticky = "nswe", padx = 20, pady = 20)

        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row = 1, column = 0, sticky = "nswe", padx = 20, pady = 10)

        right_frame = customtkinter.CTkFrame(self)
        right_frame.grid(row = 1, column = 1, sticky = "nswe", padx = 20, pady = 10)

        #Components
        editcompany = EditCompany(self, top_frame, self.values)
        capitaltree = CapitalTree.CapitalTree(self, right_frame, values)
        aid = AidTree.AidTree(self,left_frame, values)