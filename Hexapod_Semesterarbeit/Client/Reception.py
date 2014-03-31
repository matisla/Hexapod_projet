'''
Created on 24 mars 2014

@author: Matthieu
'''

import socket, sys, threading


class Reception(threading.Thread):
    
    """
    Thread Client qui permet de receptions les information qui vienne de l'hexapod
    
    """
    
    def __init__(self, conn,  gui=None, Debug=True):

        self.debug = Debug

        threading.Thread.__init__(self)                
        self.setName("Reception")
        
        self.connexion = conn
        
        self.ui = gui
    
    def run(self):
        
        while 1:
            # cycle normal
            
            message = self.connexion.recv(1024)
            message = message.decode()
            
            if message.upper() == "END":
                
                if self.debug is True:
                    print("connexion termine")
                
                break
            
            else:
                self.logger(message)
        
        if self.debug is True:
            print("fin de la connexion")    
        
        self.connexion.close()
    
    
    
    def logger(self, message):
        if self.ui is not None:
            self.ui.log(message)
        
        else:
            if self.debug is True:
                print("[Attention]: pas de log attribue")
            
            print(message)
            
    def setUi(self, gui):
        self.ui = gui
        
        if self.debug is True:
            print("connexion: thread Reception - interface graphique PRET")

if __name__ == '__main__':
    print("lancer le Main")