from tkinter import*
import customtkinter
import requests

class ExcelPopUp(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
        WIDTH = 330
        HEIGHT = 100
        
        self.root = customtkinter.CTkToplevel()
        self.root.title('Saved')
        self.root.geometry(f"{WIDTH}x{HEIGHT}")

        self.root.columnconfigure((0), weight=1)
        self.root.rowconfigure((1), weight=1)

        main_frame = customtkinter.CTkFrame(self.root,
                                height= 30, 
                                corner_radius=0,
                            )
        main_frame.grid(row = 0, column = 0, sticky = "nswe")




        text = customtkinter.CTkLabel(main_frame, text="Saved succesfully. Check your download folder")
        text.grid(row = 0, column= 0, columnspan= 2, padx = 10, pady= 10 )

        ok_btn = customtkinter.CTkButton(main_frame, text="Ok", command= self.root.destroy)
        ok_btn.grid(row = 1, column= 0, padx = 10, pady= 10 )
        
    



      
