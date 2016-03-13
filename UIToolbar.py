from Tkinter import *;

class UIToolbar:
    def __init__(self, parent):
        self.toolbar = Frame(parent)

        self.spoof_btn = Button(self.toolbar, text='Start Spoofing')
        self.spoof_btn.pack(side=LEFT, padx=2, pady=2)

        self.defend_btn = Button(self.toolbar, text='Start Defending')
        self.defend_btn.pack(side=LEFT, padx=2, pady=2)

        self.toolbar.pack(side=TOP, fill=X)
