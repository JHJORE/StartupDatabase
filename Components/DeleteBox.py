from tkinter import*
import customtkinter
import requests


from sql_app.crud import delete_Company

class DeleteBox(Frame):

    def __init__(self, parent, tree):
        Frame.__init__(self, parent)
        self.tree = tree

        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
        WIDTH = 330
        HEIGHT = 100

    
        self.root = customtkinter.CTkToplevel()
        self.root.title('Delete')
        self.root.geometry(f"{WIDTH}x{HEIGHT}")

        self.root.columnconfigure((0), weight=1)
        self.root.rowconfigure((1,2,3,4,5,6,7,8,9), weight=1)

        main_frame = customtkinter.CTkFrame(self.root,
                                height= 30, 
                                corner_radius=0,
                            )
        main_frame.grid(row = 0, column = 0, sticky = "nswe")




        text = customtkinter.CTkLabel(main_frame, text="Do you want to delete this company?")
        text.grid(row = 0, column= 0, columnspan= 2, padx = 10, pady= 10 )

        yes_btn = customtkinter.CTkButton(main_frame, text="Yes", command= self.remove_company)
        yes_btn.grid(row = 1, column= 0, padx = 10, pady= 10 )
        
        no_btn = customtkinter.CTkButton(main_frame, text="No", command= self.root.destroy)
        no_btn.grid(row = 1, column= 1, padx = 10, pady= 10 )

    def remove_company(self):
        company = self.tree.focus()
        row = self.tree.item(company)
        values = row.get('values')
        orgnumber = values[1]
        self.tree.delete(company)

        URL = "http://127.0.0.1:8000/Company/" + str(orgnumber) + "/delete"
        PARAMS = {"OrgNumber": orgnumber}
        requests.delete(url = URL, params = PARAMS)
        self.root.destroy()


      
