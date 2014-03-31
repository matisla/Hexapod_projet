'''
Created on 24 mars 2014

@author: Matthieu
'''

import socket, sys, threading


class Emission(threading.Thread):
    
    """
    Thread Client qui permet d'envoyer les commandes vers l'hexapod
    
    """
    
    def __init__(self, conn,  gui=None, Debug=True):
        
        self.debug = Debug
        
        threading.Thread.__init__(self)
        
        self.setName("Emission")
        
        self.connexion = conn
        self.ui = gui
        
        self.listMsg = list("")
        
        
    def run(self):
        end = False
        
        while end == False:
            for message in self.listMsg:
                
                if message.upper() == "END":
                    end = True
                    
                    if self.debug is True:
                        print("Emission: deconnexion en cours ...")                   
                    
                    self.connexion.send(message.encode())
                    self.listMsg.remove(message)
                    break

                self.connexion.send(message.encode())
                self.listMsg.remove(message)
                    
    
    def logger(self, message):
        if self.ui is not None:
            self.ui.log(message)
        
        else:
            if self.debug is True:
                print("[Attention]: pas de log attribue")
                
            print(message)
    
    def sendMsg(self, message):
        self.listMsg.append(message)
    
    def setUi(self, gui):
        self.ui = gui
        
        if self.debug is True: 
            print("connexion: thread Emission  - interface graphique PRET")
        
if __name__ == '__main__':
    print("lancer le Main")