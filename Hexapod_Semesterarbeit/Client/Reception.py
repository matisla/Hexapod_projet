'''
Created on 24 mars 2014

@author: Matthieu
'''

import socket, sys, threading


class Reception(threading.Thread):
    
    """
    Thread Client qui permet de receptions les information qui vienne de l'hexapod
    
    """
    
    def __init__(self, conn,  gui=None):

        threading.Thread.__init__(self)
        
        self.connexion = conn
        
        self.ui = gui
    
    def run(self):
        
        while 1:
            # cycle normal
            
            message = self.connexion.recv(1024)
            message = message.decode()
            
            if message.upper() == "END":
                self.logger("connexion termine")
                break
            
            else:
                self.logger(message)
            
        self.connexion.close()
    
    
    
    def logger(self, message):
        if self.ui is not None:
            self.ui.log(message)
        
        else:
            print(message)
        

if __name__ == '__main__':
    print("lancer le Main")