'''
Created on 27 mars 2014

@author: Matthieu
'''

from tkinter import *

class Receiver(Frame):
    '''
    Gere les entrees dans la GUI
    '''


    def __init__(self, win):
        '''
        Constructor
        '''
        self.fenetre = win
  
        self.box = Frame(self.fenetre)
        self.box.pack(side="right", padx=10, pady=10)
        
        self.initLoger()
  
    def initLoger(self):
        """
        log des commandes
        """

        self.sendedbox = Frame(self.box, width=100, height=10)
        self.sendedbox.pack(side="top", fill="both")
        
        self.scrollbar = Scrollbar(self.sendedbox)
        self.scrollbar.pack(side="right", fill=Y )

        self.sended = Listbox(self.sendedbox, yscrollcommand=self.scrollbar.set, bg="white", width=40)
        self.sended.pack(side="top")   
        
    
    def log(self, message):
        self.sended.insert(0, message)
        
if __name__ == "__main__" :
    fenetre = Tk()
    fenetre.title("Commande")
    
    myReceiver = Receiver(fenetre)
    myReceiver.mainloop()

