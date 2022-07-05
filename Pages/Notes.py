from tkinter import*
import customtkinter

from Components import NavBar, NoteTree, NoteMenuBar

class Notes(Frame):

    def __init__(self, parent, controller,values):
        Frame.__init__(self, parent)
        self.OrgNumber = values[1]

        #frames
        top_frame = customtkinter.CTkFrame(self,
                                height= 200, 
                                corner_radius=0,
                            )
        top_frame.grid(row = 0, column = 0, sticky = "nswe")

        mid_frame = customtkinter.CTkFrame(self)
        mid_frame.grid(row = 1, column = 0, sticky = "nswe", padx = 10, pady = 10)

        tree_frame = customtkinter.CTkFrame(self)
        tree_frame.grid(row = 2, column = 0, sticky = "nswe", padx = 10, pady = 10)
   
        bottom_frame = customtkinter.CTkFrame(self)
        bottom_frame.grid(row = 3, column = 0, sticky = "nswe", padx = 10, pady = 10)


        #components
        vscroll = Scrollbar(bottom_frame)
        vscroll.pack(side=RIGHT, fill= Y)

        textbox = Text(bottom_frame,width=100, height=15)
        textbox.pack()

        vscroll.config(command=textbox.yview)

        navbar = NavBar.NavBar(parent, controller, top_frame)
        trash = NoteMenuBar.NoteMenuBar(parent,mid_frame, textbox, values)
        tree= NoteTree.NoteTree(self, tree_frame, self.OrgNumber, textbox)




