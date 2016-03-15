from Tkinter import *
from Sniffer import Sniffer
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


class NetworkPlotter:
    def __init__(self, parent):
        self.figure = Figure(figsize=(5,5), dpi=100)
        self.a = self.figure.add_subplot(1,1,1,axisbg='black')
        self.canvas = FigureCanvasTkAgg(self.figure, parent)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=True)
        self.ani = animation.FuncAnimation(self.figure, self.animate ,interval=1000)
        self.sniffer = Sniffer(1, 'Sniffer-1', 1)
        self.sniffer.start()

    def animate(self, i):
        pullData = open('sample_data.txt', 'r').read()
        dataArray = pullData.split('\n')
        xar = []
        yar = []
        for line in dataArray:
            if len(line)>1:
                x,y = line.split(',')
                xar.append(x)
                yar.append(y)
        self.a.clear()
        self.a.plot(xar,yar)
