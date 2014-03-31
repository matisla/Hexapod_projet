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
                    if self.debug is True:
                        print("[Client]: Emission      >> fin de la communication")
                        
                    end = True
                    
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
                print("[Client]: Emission      >> Attention pas de log attribue")
                
            print(message)
    
    def sendMsg(self, message):
        self.listMsg.append(message)
    
    def setUi(self, gui):
        self.ui = gui
        
        if self.debug is True: 
            print("[Client]: Emission      >> Thread Emission - Interface Graphique PRET")
        
if __name__ == '__main__':
    print("lancer le Client SVP")