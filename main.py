from Tkinter import *
from UIMenu import UIMenu
from UIToolbar import UIToolbar
from UIStatusbar import UIStatusbar
from NetworkPlotter import NetworkPlotter
from Packet import Packet
from DisplayPacket import DisplayPacket 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

root = Tk()

uiMenu = UIMenu(root)
root.config(menu=uiMenu.menu)
uiToolbar = UIToolbar(root)
uiStatusbar = UIStatusbar(root)
networkPlotter = NetworkPlotter(root)

myPacket = Packet(111,222,333,444)
display = DisplayPacket(root, myPacket) 

root.mainloop()
