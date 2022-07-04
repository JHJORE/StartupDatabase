from tkinter import*
import customtkinter
from Components.FilesView import FilesView

class Notes(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        


        # Frames
        top_frame = customtkinter.CTkFrame(self,
                                height= 10, 
                                corner_radius=0,
                            )
        top_frame.grid(row = 0, column = 0, sticky = "nswe")

        title_frame = customtkinter.CTkFrame(self)
        title_frame.grid(row = 1, column = 0, sticky = "nswe", padx = 20, pady = 10)

        bottom_frame = customtkinter.CTkFrame(self)
        bottom_frame.grid(row = 2, column = 0, sticky = "nswe", padx = 20, pady = 10)

        vscroll = Scrollbar(bottom_frame)
        vscroll.pack(side=RIGHT, fill= Y)

        textbox = Text(bottom_frame,width=200, height=200)
        textbox.pack()

        vscroll.config(command=textbox.yview)

        #menu

        # filesview = FilesView(self, self, textbox)

        title = customtkinter.CTkLabel(master=top_frame,
                                    width=120,
                                    text="Company Name",
                                    height=45,
                                    corner_radius=8)
        title.grid(row =0, column= 0)



