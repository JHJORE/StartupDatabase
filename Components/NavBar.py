import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from Pages import HomePage

class NavBar(tk.Frame):
    def __init__(self, parent, controller, top_frame):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        folder_img = ImageTk.PhotoImage(Image.open("./Constants/fi-og-img.png").resize((70,70),  Image.LANCZOS))
        self.icon = customtkinter.CTkButton(top_frame, image = folder_img,text="",borderwidth=0, width=70, height= 70, compound= "left", command=self.openHome)
        self.icon.grid(row=0, column=0, padx=20, pady=10)

        folder_img = ImageTk.PhotoImage(Image.open("./Constants/database.png").resize((40,40),  Image.LANCZOS))
        self.database_btn = customtkinter.CTkButton(top_frame, image = folder_img,text="", width=50, height= 50, compound= "left", command = self.openHome)
        self.database_btn.grid(row=0, column=1, padx=10, )

        folder_img = ImageTk.PhotoImage(Image.open("./Constants/company.png").resize((40,40),  Image.LANCZOS))
        company_btn = customtkinter.CTkButton(top_frame, image = folder_img,text="", width=50, height= 50, compound= "left" )
        company_btn.grid(row=0, column=2, padx=20, pady=10)

        folder_img = ImageTk.PhotoImage(Image.open("./Constants/list.png").resize((40,40),  Image.LANCZOS))
        list_btn = customtkinter.CTkButton(top_frame, image = folder_img,text="", width=50, height= 50, compound= "left" )
        list_btn.grid(row=0, column=3, padx=20, pady=10)

        self.mode_switch = customtkinter.CTkSwitch(top_frame, text = "Dark Mode", command= self.switchmode, onvalue= "on", offvalue= "off")
        self.mode_switch.grid(row=0, column=9, padx=10, pady=10)

        self.switchmode

    def switchmode(self):
        state = self.mode_switch.get()
        if(state == "on"):
            customtkinter.set_appearance_mode("Dark")
            self.controller.dark_mode()
        else:
            customtkinter.set_appearance_mode("System")
            self.controller.normal_mode()

    def openHome(self):
        self.controller.show_frame(HomePage.HomePage(self.parent, self.controller))

