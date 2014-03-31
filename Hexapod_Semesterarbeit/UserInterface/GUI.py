'''
Created on 19 mars 2014

@author: Matthieu
Version: 1.00


Option:
- mettre en place le cadre pour la video.
'''

import socket, sys, threading
from tkinter import *

from UserInterface import Sender, Receiver


class GUI(threading.Thread):
    
    def __init__(self):
        
        threading.Thread.__init__(self)
        self.start()
        
    def run(self):
        
        self.fenetre = Tk()
        self.fenetre.title("Commande")
        
        self.sender   = Sender.Sender(self.fenetre)
        self.receiver = Receiver.Receiver(self.fenetre)
        
        self.fenetre.mainloop()
        
    def quitter(self):
        self.fenetre.quit()
        
    def log(self, message):
        self.receiver.log(message)
        
        
if __name__ == '__main__':
    test = GUI()