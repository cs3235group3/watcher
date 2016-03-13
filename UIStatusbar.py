from Tkinter import *

class UIStatusbar:
    def __init__(self, parent):
        self.statusbar = Label(parent, text='Statusbar', bd=1, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)
