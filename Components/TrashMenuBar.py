from tkinter import*
import customtkinter
class TrashMenuBar(Frame):
    def __init__(self, parent, top_frame ):
        Frame.__init__(self, parent)
        self.top_frame = top_frame

        save_btn = customtkinter.CTkButton(top_frame, text="Save")
        save_btn.grid(row = 0, column=0, padx = 10, pady = 10 )

        delete_btn = customtkinter.CTkButton(top_frame, text="Delete")
        delete_btn.grid(row = 0, column=1, padx = 10, pady = 10 )

        
        open_btn = customtkinter.CTkButton(top_frame, text="Open Note")
        open_btn.grid(row = 0, column=3, padx = 10, pady = 10 )
        

