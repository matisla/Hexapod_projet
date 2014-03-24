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


fenetre = Tk()
fenetre.title("Commande")

def cmdsend():
    sendedbox = Frame(fenetre, width=100, height=10)
    sendedbox.pack(side="top")
    
    sended = Label(sendedbox, width=40)
    sended.pack(side="top")
    
def cmdbox():
    cmdbox = Frame(fenetre)
    cmdbox.pack(side="bottom")

    cmdSend = StringVar()
    ligne_texte = Entry(cmdbox, textvariable=cmdSend, width=40)
    ligne_texte.pack(side="left")

    boutton_send = Button(cmdbox, text="send", width=10)
    boutton_send.pack(side="right")

def fenetreeur():
    
    fenetrebox = Frame(fenetre)
    fenetrebox.pack(side="top", pady=10)
    
    boutton_fw = Button(fenetrebox, text="fw", width=10)
    boutton_fw.pack(side="top")
    
    boutton_bw = Button(fenetrebox, text="bw", width=10)
    boutton_bw.pack(side="bottom")
    
    boutton_left = Button(fenetrebox, text="left", width=10)
    boutton_left.pack(side="left")

    boutton_right = Button(fenetrebox, text="right", width=10)
    boutton_right.pack(side="right")    
    
    
    fenetreboxR = Frame(fenetre)
    fenetreboxR.pack(side="top", pady=10)
    
    boutton_leftR = Button(fenetreboxR, text="Rot. left", width=10)
    boutton_leftR.pack(side="left")

    boutton_rightR = Button(fenetreboxR, text="Rot. right", width=10)
    boutton_rightR.pack(side="right")    
    
cmdsend()
cmdbox()
fenetreeur()
fenetre.mainloop()

"""
if __name__ == '__main__':
    cmdsend()
    cmdbox()
    fenetreeur()
    fenetre.mainloop()
"""