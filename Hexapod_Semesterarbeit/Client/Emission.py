'''
Created on 24 mars 2014

@author: Matthieu
'''

import socket, sys, threading

class Emission(threading.Thread):
    
    """
    Thread Client qui permet d'envoyer les commandes vers l'hexapod
    
    """
    
    def __init__(self, conn):
        
        threading.Thread.__init__(self)
        
        self.connexion = conn
        
        self.listMsg = list("hello")
        
    def run(self):
        end = False
        
        while end == False:
            for message in self.listMsg:
                if message.upper() == "END":
                    end = True
                    break
            
                self.connexion.send(message.encode())
        
        self.deconnexion()
        
        
    def sendMsg(self, message):
        """
        envoie le message
        """
        self.listMsg.append(message)
        
    def deconnexion(self):
        print("deconnexion en cours ...")
        self.connexion.close()
    

if __name__ == '__main__':
    print("lancer le Main")