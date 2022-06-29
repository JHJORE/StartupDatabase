def AnnotatedEntry(master, name="An annoted entry box"):
    '''
    As a little extra, name is a keyword-argument, which defaults to "An annotated
    entry box."
    '''
    import tkinter as tk
    overlord = tk.Frame(master, height=5, width=40)
    labeller = tk.Label(overlord, text=name, font="Times 14 bold")
    labeller.grid(sticky='new')

    inputter = tk.Entry(overlord, font="Times 14 bold")
    inputter.grid(sticky='sew', pady=(10,0))

    return overlord