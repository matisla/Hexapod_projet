'''
Created on 27 mars 2014

@author: Matthieu
'''

from tkinter import *

class Receiver():
    '''
    Gere les entrees dans la GUI
    '''


    def __init__(self, win, Debug=True):
        
        self.debug = Debug
        
        self.fenetre = win
  
        self.box = Frame(self.fenetre)
        self.box.pack(side="bottom", expand=True, fill="x", padx=10, pady=10)
        
        self.initLoger()
  
    def initLoger(self):
        """
        log des commandes
        """

        self.sendedbox = Frame(self.box)
        self.sendedbox.pack(side="bottom", expand=True, fill="both")
        
        self.scrollbar = Scrollbar(self.sendedbox)
        self.scrollbar.pack(side="right", fill="y")

        self.sended = Listbox(self.sendedbox, yscrollcommand=self.scrollbar.set, bg="white", width=60)
        self.sended.pack(side="bottom", expand=True, fill="both")   
        
    
    def log(self, message):
        if self.debug is True:
            print("[GUI]   : receiver      >> message logger: " + message)
        
        self.sended.insert(END, message)
        
        
if __name__ == "__main__" :
    fenetre = Tk()
    fenetre.title("Commande")
    
    myReceiver = Receiver(fenetre)
    myReceiver.mainloop()