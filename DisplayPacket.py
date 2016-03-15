from Tkinter import *
from Packet import Packet

class DisplayPacket(object):

    def __init__(self, parent, packet):#packet of type Packet
        self.senderIP = packet.getSenderIp()
        self.senderMAC = packet.getSenderMac()
        self.DstIP = packet.getDstIp()
        self.DstMAC = packet.getDstMac()
        
        self.totalText = "Sender IP:\n%d\nSender MAC:\n%d\nDestination IP:\n%d\nDestination MAC:\n%d" % (self.senderIP,self.senderMAC,self.DstIP,self.DstMAC) 
        self.title = "Packet Details\n" 

        self.text = Text(parent, height=10, width = 32)
        self.text.tag_configure('big', font=('Verdana', 20, 'bold'))
        self.text.insert(END,self.title, 'big') 
        self.text.pack(side=RIGHT, fill=BOTH)
        self.text.insert(END, self.totalText)


#root = Tk()
#myPacket = Packet(111,222,333,444)
#display = DisplayPacket(root, myPacket)
#mainloop()

