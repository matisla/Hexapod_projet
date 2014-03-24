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

import cmdServos

class User_Interface(Frame):
    
    def __init__(self):
        
        self.fenetre = Tk()
        self.fenetre.title("Commande")
        
        self.output()
        self.input()
        
        self.fenetre.mainloop()
        


    def cmdSend(self):
        
        """
        Commande: envoie d'une commande mannuelle
        """
        
        #Emission.sendMsg()
        
        self.sended.insert(0,self.varSend.get()) 
        self.varSend.initialize("")

    
    def fwcmd(self):
        
        """
        Commande: envoie d'une commande mannuelle
                  avancer
        """
        self.sended.insert(0,"Forward")

    def bwcmd(self):
        
        """
        Commande: envoie d'une commande mannuelle
                  reculer
        """
        self.sended.insert(0, "Backward")
               
    def leftcmd(self):
        
        """
        Commande: envoie d'une commande mannuelle
                  aller a gauche
        """
        self.sended.insert(0,"Left")
    
    def rightcmd(self):
        
        """
        Commande: envoie d'une commande mannuelle
                  aller a droite
        """
        self.sended.insert(0,"Right")
    
    def Rleftcmd(self):
        
        """
        Commande: envoie d'une commande mannuelle
                  aller a gauche
        """
        self.sended.insert(0,"Rotation Left")
    
    def Rrightcmd(self):
        
        """
        Commande: envoie d'une commande mannuelle
                  aller a droite
        """
        self.sended.insert(0,"Rotation Right")
            
    def log(self, message):
        """
        ajouter un message au log
        """
        
        self.sended.insert(0, message)
    
    
    
    """
    Initialisation
    """             
    
    def input(self):
        """
        la partie commande
        """
        self.inputbox = Frame(self.fenetre)
        self.inputbox.pack(side="right", padx=10, pady=10)
        
        self.init_loger()
        
    def output(self):
        """
        la partie information
        """
        self.outputbox = Frame(self.fenetre)
        self.outputbox.pack(side="left", padx=10, pady=10)
        
        self.init_controler()
        self.init_sender()
               
    def init_controler(self):
        """
        Panneau de controle manuelle Translation
        """
        self.fenetrebox = Frame(self.outputbox)
        self.fenetrebox.pack(side="top", pady=10)
        
        self.boutton_fw = Button(self.fenetrebox, command=self.fwcmd, text="fw", width=10)
        self.boutton_fw.pack(side="top")
        
        self.boutton_bw = Button(self.fenetrebox, command=self.bwcmd, text="bw", width=10)
        self.boutton_bw.pack(side="bottom")
        
        self.boutton_left = Button(self.fenetrebox, command=self.leftcmd, text="left", width=10)
        self.boutton_left.pack(side="left")
        
        self.boutton_right = Button(self.fenetrebox, command=self.rightcmd, text="right", width=10)
        self.boutton_right.pack(side="right")    
        
        """
        Panneau de controle manuelle Rotation
        """
        self.fenetreboxR = Frame(self.outputbox)
        self.fenetreboxR.pack(side="top", pady=10)
        
        self.boutton_leftR = Button(self.fenetreboxR, command=self.Rleftcmd, text="Rot. left", width=10)
        self.boutton_leftR.pack(side="left")
        
        self.boutton_rightR = Button(self.fenetreboxR, command=self.Rrightcmd, text="Rot. right", width=10)
        self.boutton_rightR.pack(side="right")
        
    def init_sender(self):
        """
        envoyer des commandes en manuelle
        """
        
        self.cmdbox = Frame(self.outputbox)
        self.cmdbox.pack(side="bottom")
    
        self.varSend = StringVar()
        self.ligne_texte = Entry(self.cmdbox, textvariable=self.varSend, width=40)
        self.ligne_texte.pack(side="left")
    
        self.boutton_send = Button(self.cmdbox, command=self.cmdSend, text="send", width=10)
        self.boutton_send.pack(side="right")


    def init_loger(self):
        """
        log des commandes
        """

        self.sendedbox = Frame(self.inputbox, width=100, height=10)
        self.sendedbox.pack(side="top")
        
        self.scrollbar = Scrollbar(self.sendedbox)
        self.scrollbar.pack(side="right", fill=Y )

        
        self.sended = Listbox(self.sendedbox, yscrollcommand=self.scrollbar.set, bg="white", width=40)
        self.sended.pack(side="top")    
    
    
if __name__ == '__main__':
    test = User_Interface()