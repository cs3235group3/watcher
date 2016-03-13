from Tkinter import *;

class UIToolbar:
    def __init__(self, parent):
        self.toolbar = Frame(parent)

        self.btn = Button(self.toolbar, text='Button')
        self.btn.pack(side=LEFT, padx=2, pady=2)

        self.toolbar.pack(side=TOP, fill=X)