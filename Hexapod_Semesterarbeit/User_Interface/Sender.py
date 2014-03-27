'''
Created on 27 mars 2014

@author: Matthieu
'''
from tkinter import *


class Sender(Frame):
    '''
    gere la partie envoie de commande de la GUI
    '''


    def __init__(self, win):
        '''
        Constructor
        '''
        self.fenetre  = win
        self.emetteur = None
        
        self.box = Frame(self.fenetre)
        self.box.pack(side="left", padx=10, pady=10)
        
        self.initControler()
        self.initSender()
        
        
    def initControler(self):
        """
        Panneau de controle manuelle Translation
        """
        self.fenetrebox = Frame(self.box)
        self.fenetrebox.pack(side="top", pady=10)
        
        self.boutton_fw = Button(self.fenetrebox, command=lambda: self.cmd("fw"), text="fw", width=10)
        self.boutton_fw.pack(side="top")
        
        self.boutton_bw = Button(self.fenetrebox, command=lambda: self.cmd("bw"), text="bw", width=10)
        self.boutton_bw.pack(side="bottom")
        
        self.boutton_left = Button(self.fenetrebox, command=lambda: self.cmd("le"), text="left", width=10)
        self.boutton_left.pack(side="left")
        
        self.boutton_right = Button(self.fenetrebox, command=lambda: self.cmd("ri"), text="right", width=10)
        self.boutton_right.pack(side="right")    
        
        """
        Panneau de controle manuelle Rotation
        """
        self.fenetreboxR = Frame(self.box)
        self.fenetreboxR.pack(side="top", pady=10)
        
        self.boutton_leftR = Button(self.fenetreboxR, command=lambda: self.cmd("rl"), text="Rot. left", width=10)
        self.boutton_leftR.pack(side="left")
        
        self.boutton_rightR = Button(self.fenetreboxR, command=lambda: self.cmd("rr"), text="Rot. right", width=10)
        self.boutton_rightR.pack(side="right")
        
        
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
            self.emetteur.sendMsg(cmd)
        else:
            print(cmd)
        
    def cmdSend(self):
        self.cmd(self.varSend.get()) 
        self.varSend.initialize("")

if __name__ == "__main__" :
    
    fenetre = Tk()
    fenetre.title("Commande")
    mySender = Sender(fenetre)