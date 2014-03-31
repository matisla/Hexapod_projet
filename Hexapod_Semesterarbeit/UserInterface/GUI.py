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
    
    def __init__(self, Debug=True):
        
        self.debug = Debug
        
        threading.Thread.__init__(self)
        self.setName("GUI")
        
        
        self.fenetre = Tk()
        self.fenetre.title("Commande")
        
        self.senderbox = Frame(self.fenetre)
        self.senderbox.pack(side="left",  expand=False, padx=5, pady=5)
        
        self.sender = Sender.Sender(self.senderbox, Debug=self.debug)
        
        self.receiverbox = Frame(self.fenetre)
        self.receiverbox.pack(side="right", expand=True, fill="x", padx=5, pady=5)
        
        self.receiver = Receiver.Receiver(self.receiverbox, Debug=self.debug)
        
        self.start()
        
        
        
    def run(self):
        
        if self.debug is True:
            print("[GUI]   : GUI           >> Interface Graphique operationnel")
            
        self.fenetre.mainloop()
        
        
    def quitter(self):
        self.fenetre.quit()
    
    def setConnexion(self, conn):
        self.sender.setConnexion(conn)
    
    def log(self, message):
        
        try:
            self.receiver.log(message)
        
        except:
            if self.debug is True:
                print("[GUI]   : GUI           >> Attention connexion avec le logger non existant !")
            print("message: " + message)
            
            
if __name__ == '__main__':
    test = GUI()
    