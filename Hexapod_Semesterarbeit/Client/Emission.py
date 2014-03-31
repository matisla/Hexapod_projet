'''
Created on 24 mars 2014

@author: Matthieu
'''

import socket, sys, threading


class Emission(threading.Thread):
    
    """
    Thread Client qui permet d'envoyer les commandes vers l'hexapod
    
    """
    
    def __init__(self, conn,  gui=None):
        
        threading.Thread.__init__(self)
        
        self.connexion = conn
        self.ui = gui
        
        self.listMsg = list("")
        
        
    def run(self):
        end = False
        
        while end == False:
            for message in self.listMsg:
                
                if message.upper() == "END":
                    end = True
                    self.logger("deconnexion en cours ...")
                    self.connexion.send(message.encode())
                    self.listMsg.remove(message)
                    

                self.connexion.send(message.encode())
                self.listMsg.remove(message)
                    
    
    def logger(self, message):
        if self.ui is not None:
            self.ui.log(message)
        
        else:
            print(message)
    
    def sendMsg(self, message):
        self.listMsg.append(message)
    

if __name__ == '__main__':
    print("lancer le Main")