from Tkinter import *;
import subprocess 

class UIToolbar:
    def __init__(self, parent):
        self.toolbar = Frame(parent)

        self.spoof_btn = Button(self.toolbar, text='Start Spoofing')
        self.spoof_btn.pack(side=LEFT, padx=2, pady=2)

        self.defend_btn = Button(self.toolbar, text='Start Defending')
        self.defend_btn.pack(side=LEFT, padx=2, pady=2)

        self.pause_btn = Button(self.toolbar, text='Pause')
        self.pause_btn.pack(side=LEFT, padx=2, pady=2)

        self.start_btn = Button(self.toolbar, text='Start Tracking')
        self.start_btn.pack(side=LEFT, padx=2, pady=2)
        self.toolbar.pack(side=TOP, fill=X)


    def startSpoof(self):
        #subprocess.call(["java","attacker"])
        pass 

    def startDefence(self):
        #subprocess.call(["java","defender"])
        pass 
