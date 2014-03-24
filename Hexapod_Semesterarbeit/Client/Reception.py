'''
Created on 24 mars 2014

@author: Matthieu
'''

import socket, sys, threading
from GUI import *

class Reception(threading.Thread):
    
    """
    Thread Client qui permet de receptions les information qui vienne de l'hexapod
    
    """
    
    def __init__(self, HOST='192.168.1.1', PORT=50000):

        threading.Thread.__init__(self)
        
        self.ip   = HOST
        self.port = PORT
        
        self.connexion = self.connexion()
        
    
    def run(self):

        while 1:
            # cycle normal
            
            msg_recu = self.connexion.recv(1024)
            self.logger(msg_recu)
            
            
            if msg_recu.upper() == "END":
                self.connexion.close()
                break
        
        # deconnexion
        self.deconnexion()
              
    def logger(self, message):
        """
        reception d'un message et l'envoyer dans le log
        """
        
        print(message)
        
    def connexion(self):
         
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            conn.connect( (self.ip, self.port) )
            print ("Connexion etablis avec succes")
        
        except socket.error:
            print ("La liaison du socket a l'adresse choisie a echoue.")
            sys.exit()
            
        return conn
        
    def deconnexion(self):
        print("deconnexion en cours ...")
        self.connexion.close()
    

if __name__ == '__main__':
    myThread = Reception()
    myThread.start()