from tkinter import*
from tkinter import ttk
import customtkinter
import sqlite3
from Components import AidTree, CapitalTree, EditCompany

class CompanyView(Frame):

    def __init__(self, parent, values):
        Frame.__init__(self, parent)
        self.values = values
        print(values)

        # customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        # customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
        # WIDTH = 820
        # HEIGHT = 600


        # self = customtkinter.CTk()
        # self.title('Startup Database')
        # self.geometry(f"{WIDTH}x{HEIGHT}")
        # conn = sqlite3.connect('sql_app.db')
        # cursor = conn.cursor()

        # self.columnconfigure((0,1), weight=1)
        # self.rowconfigure((1,1), weight=1)
        # #Style
        # style = ttk.Style()
        # style.theme_use("default")
        # style.configure("Treeview",
        # foreground ="black",
        # rowheight = 23,
        # )

        #Frames
        top_frame = customtkinter.CTkFrame(self)
        top_frame.grid(row = 0, column = 0,  columnspan=2, sticky = "nswe", padx = 20, pady = 20)

        left_frame = customtkinter.CTkFrame(self)
        left_frame.grid(row = 1, column = 0, sticky = "nswe", padx = 20, pady = 10)

        right_frame = customtkinter.CTkFrame(self)
        right_frame.grid(row = 1, column = 1, sticky = "nswe", padx = 20, pady = 10)

        #table
        editcompany = EditCompany(self, top_frame, self.values)
        #tree kapitalutvidelse
        #capitaltree = CapitalTree.CapitalTree(self, right_frame, values)


        # #tree AID
        #aid = AidTree.AidTree(self,left_frame, values)





        # tree.bind("<ButtonRelease-1>", clicked)