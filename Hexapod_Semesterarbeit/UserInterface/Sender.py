'''
Created on 27 mars 2014

@author: Matthieu
'''
from tkinter import *


class Sender():
    '''
    gere la partie envoie de commande de la GUI
    '''


    def __init__(self, win, Debug=True):
        
        self.debug = Debug
        
        self.fenetre  = win
        self.emetteur = None
        
        self.box = Frame(self.fenetre)
        self.box.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        
        self.initControler()
        self.initSender()
        
        
    def initControler(self):
        """
        Panneau de controle manuelle Translation
        """
        self.fenetrebox = Frame(self.box)
        self.fenetrebox.pack(side="top", pady=10)
        
        self.boutton_fw = Button(self.fenetrebox, command=lambda: self.cmd("fw"), text="fw", width=10)
        self.boutton_fw.grid(row=0, column=1)
        
        self.boutton_bw = Button(self.fenetrebox, command=lambda: self.cmd("bw"), text="bw", width=10)
        self.boutton_bw.grid(row=1, column=1)
        
        self.boutton_left = Button(self.fenetrebox, command=lambda: self.cmd("le"), text="left", width=10)
        self.boutton_left.grid(row=1, column=0)
        
        self.boutton_right = Button(self.fenetrebox, command=lambda: self.cmd("ri"), text="right", width=10)
        self.boutton_right.grid(row=1, column=2)
        
        """
        Panneau de controle manuelle Rotation
        """
        self.fenetreboxR = Frame(self.box)
        self.fenetreboxR.pack(side="top", pady=10)
        
        self.boutton_leftR = Button(self.fenetreboxR, command=lambda: self.cmd("rl"), text="Rot. left", width=10)
        self.boutton_leftR.grid(row=0, column=0)
        
        self.boutton_rightR = Button(self.fenetreboxR, command=lambda: self.cmd("rr"), text="Rot. right", width=10)
        self.boutton_rightR.grid(row=0, column=1)
        
        
    def initSender(self):
        """
        envoyer des commandes en manuelle
        """
        
        self.cmdbox = Frame(self.box)
        self.cmdbox.pack(side="bottom")
    
        self.varSend = StringVar()
        self.ligne_texte = Entry(self.cmdbox, textvariable=self.varSend, width=40)
        self.ligne_texte.pack(side="left")
    
        self.boutton_send = Button(self.cmdbox, command=self.cmdSend, text="send", width=10)
        self.boutton_send.pack(side="right")


    def cmd(self, cmd):
        if self.emetteur is not None:
            if self.debug is True:
                print("[GUI]   : Sender        >> commande envoye: " + cmd)
            
            self.emetteur.sendMsg(cmd)
                
        else:
            print(cmd)
        
    def cmdSend(self):
        self.cmd(self.varSend.get()) 
        self.varSend.initialize("")
        
    def setConnexion(self, conn):
        self.emetteur = conn
        
        if self.debug is True:
            print("[GUI]   : Sender        >> connexion UI Emission - Thread Emetteur PRET")
        
if __name__ == "__main__" :
    
    fenetre = Tk()
    fenetre.title("Commande")
    
    mySender = Sender(fenetre)
    mySender.mainloop()