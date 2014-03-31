'''
Created on 19 mars 2014

@author: Matthieu
Version: 1.00

A faire:
- mettre en place les commandes pour chaques boutons.

Option:
- mettre en place le cadre pour la video.
'''

from tkinter import *

from . import Sender, Receiver


class GUI(Frame):
    
    def __init__(self):
        
        self.fenetre = Tk()
        self.fenetre.title("Commande")
        
        self.sender   = Sender(self.fenetre)
        self.receiver = Receiver(self.fenetre)
        
        self.fenetre.mainloop()
            
    
if __name__ == '__main__':
    test = GUI()