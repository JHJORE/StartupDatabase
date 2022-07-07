from tkinter import*
import customtkinter
from Components import AidTree, CapitalTree, EditCompany, NavBar, ExcelPopUp
from ExportData import ExportCompanyExcel

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

        lowerMidle_frame = customtkinter.CTkFrame(self)
        lowerMidle_frame.grid(row = 2, column = 0, sticky = "nswe", padx = 20, pady = 10)

        bottom_frame = customtkinter.CTkFrame(self)
        bottom_frame.grid(row = 3, column = 0, sticky = "nswe", padx = 20, pady = 10)

        #Components
        navbar = NavBar.NavBar(parent, controller, top_frame)
        editcompany = EditCompany.EditCompany(self, middle_frame, self.values, controller)
        self.capitaltree = CapitalTree.CapitalTree(self, bottom_frame, values)
        self.aidtree = AidTree.AidTree(self,lowerMidle_frame, values)

        self.save_to_excel_btn = customtkinter.CTkButton(middle_frame, text = 'Export company to excel', command=self.save_as_excel)
        self.save_to_excel_btn.grid(row = 0, column = 2, sticky = "nse", pady=10, padx=10, ipadx= 30)


    def save_as_excel(self):
        ExportCompanyExcel.save_as_excel(self.values, self.aidtree.get_tree(), self.capitaltree.get_tree())
        ExcelPopUp.ExcelPopUp(self.parent)
