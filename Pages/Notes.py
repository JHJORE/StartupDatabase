from tkinter import*
import customtkinter

from Components import TrashMenuBar, NavBar, NoteTree

class Notes(Frame):

    def __init__(self, parent, controller,values):
        Frame.__init__(self, parent)
        self.OrgNumber = values[1]


        # Frames
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

        vscroll = Scrollbar(bottom_frame)
        vscroll.pack(side=RIGHT, fill= Y)

        textbox = Text(bottom_frame,width=120, height=20)
        textbox.pack()

        vscroll.config(command=textbox.yview)

      

        # menu
        
        navbar = NavBar.NavBar(parent, controller, top_frame)
        trash = TrashMenuBar.TrashMenuBar(parent,mid_frame, textbox, values)
        tree= NoteTree.NoteTree(self, tree_frame, self.OrgNumber, textbox)

        # menubar = MenuBar(self)
        

        # title = customtkinter.CTkLabel(master=top_frame,
        #                             width=12,
        #                             text="Company Name",
        #                             height=45,
        #                             corner_radius=8)
        # title.grid(row =0, column= 0)



