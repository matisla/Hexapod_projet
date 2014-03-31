'''
Created on 19 mars 2014

@author: Matthieu
Version: 1.00


Option:
- mettre en place le cadre pour la video.
'''

import threading
from tkinter import *

from UserInterface import Sender, Receiver


class GUI(threading.Thread):
    
    def __init__(self):
        
        threading.Thread.__init__(self)
        self.start()
        
    def run(self):
        
        self.fenetre = Tk()
        self.fenetre.title("Commande")
        
        self.senderbox = Frame(self.fenetre)
        self.senderbox.pack(side="left", padx=5, pady=5)
        
        self.sender = Sender.Sender(self.senderbox)
        
        self.receiverbox = Frame(self.fenetre)
        self.receiverbox.pack(side="right", padx=5, pady=5)
        
        self.receiver = Receiver.Receiver(self.receiverbox)
        
        self.fenetre.mainloop()
        
    def quitter(self):
        self.fenetre.quit()
    
    def setUi(self, gui):
        self.ui = gui
        self.receiver.setUi(gui)
        self.sender.setUi(gui)
    
    def log(self, message):
        self.receiver.log(message)
        
        
if __name__ == '__main__':
    test = GUI()
    