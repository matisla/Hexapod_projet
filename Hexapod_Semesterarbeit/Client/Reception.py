'''
Created on 24 mars 2014

@author: Matthieu
'''

import socket, sys, threading

class Reception(threading.Thread):
    
    """
    Thread Client qui permet de receptions les information qui vienne de l'hexapod
    
    """
    
    def __init__(self, conn):

        threading.Thread.__init__(self)
        
        self.connexion = conn
        
        self.ui = ""
    
    def run(self):
        
        while 1:
            # cycle normal
            
            message = self.connexion.recv(1024)
            self.logger(message)
            
            
            if message.upper() == "END":
                break
        
        # deconnexion
        self.deconnexion()
              
    def logger(self, message):
        """
        reception d'un message et l'envoyer dans le log
        """
        if self.ui == object:
            self.ui.log(message)
        
        print(message)
        
    def setUi(self, GUI):
        self.ui = GUI
        
    def deconnexion(self):
        
        print("deconnexion en cours ...")
        self.connexion.close()
    

if __name__ == '__main__':
    print("lancer le Main")