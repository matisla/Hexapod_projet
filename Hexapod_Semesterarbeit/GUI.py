'''
Created on 19 mars 2014

@author: Matthieu
'''

from tkinter import *
import os


fenetre = Tk()

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

def controleur():
    
    controlbox = Frame(fenetre)
    controlbox.pack(side="top", pady=10)
    
    boutton_fw = Button(controlbox, text="fw", width=10)
    boutton_fw.pack(side="top")
    
    boutton_bw = Button(controlbox, text="bw", width=10)
    boutton_bw.pack(side="bottom")
    
    boutton_left = Button(controlbox, text="left", width=10)
    boutton_left.pack(side="left")

    boutton_right = Button(controlbox, text="right", width=10)
    boutton_right.pack(side="right")    
    
    
    controlboxR = Frame(fenetre)
    controlboxR.pack(side="top", pady=10)
    
    boutton_leftR = Button(controlboxR, text="Rot. left", width=10)
    boutton_leftR.pack(side="left")

    boutton_rightR = Button(controlboxR, text="Rot. right", width=10)
    boutton_rightR.pack(side="right")    
    
cmdsend()
cmdbox()
controleur()
fenetre.mainloop()


if __name__ == '__main__':
    pass