from Tkinter import *
from UIMenu import UIMenu
from UIToolbar import UIToolbar
from UIStatusbar import UIStatusbar
from NetworkPlotter import NetworkPlotter
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

root.mainloop()