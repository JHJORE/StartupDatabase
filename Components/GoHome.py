from tkinter import *
import customtkinter

from Pages import HomePage

class GoHome(Frame):
    def __init__(self, parent, controller, top_frame):
        Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        go_home_btn = customtkinter.CTkButton(top_frame, text="Go Home", command= self.go_home)
        go_home_btn.grid(row=2, column=3, columnspan=1, pady=10, padx=10, ipadx= 30 )

    def go_home(self):
        new_frame = HomePage.HomePage(self.parent, self.controller)
        self.controller.show_frame(new_frame)