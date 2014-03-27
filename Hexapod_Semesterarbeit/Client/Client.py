'''
Created on 26 mars 2014

@author: Matthieu
'''

import socket, sys, threading
from Emission import *
from Reception import *

class Client():


    def __init__(self, HOST="168.192.0.32", PORT=50000):
        
        self.ip   = HOST
        self.port = PORT
        
        self.connexion()
       
    def connexion(self):
        
        # Creation du Socket

        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2) envoi d'une requete de connexion au serveur:
        
        try:
            connexion.connect( (self.ip, self.port) )
            print ("Connexion etablie avec le serveur")
        
        except socket.error:
            print ("La connexion a echoue avec le serveur.")
            sys.exit()
        
        self.thR = Reception(connexion)
        self.thE = Emission(connexion)
        
        self.thR.start()
        self.thE.start()

    def getClient(self):
        return (self.thE, self.thR)
    
if __name__ == '__main__':
    myClient = Client()