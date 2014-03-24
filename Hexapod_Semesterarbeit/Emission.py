'''
Created on 24 mars 2014

@author: Matthieu
'''

import socket, sys, threading

class Emission():
    
    """
    Thread Client qui permet d'envoyer les commandes vers l'hexapod
    
    """
    
    def __init__(self, HOST='192.168.1.1', PORT=50000):
        
        self.ip   = HOST
        self.port = PORT
        
        self.connexion = self.connexion()
        
    
    def sendMsg(self, message):
        """
        envoie le message
        """
        self.connexion.send(message)
        
        if message.upper() == "END":
            self.deconnexion()
        
        
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
    mySender = Emission()