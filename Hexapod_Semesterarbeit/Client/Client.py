'''
Created on 26 mars 2014

@author: Matthieu
'''

import socket, sys, threading
import Emission
import Reception

class Client():


    def __init__(self, HOST="168.192.0.32", PORT=50000):
        
        self.ip   = HOST
        self.port = PORT
        
        self.connexion()
       
    def connexion(self):
        
        # Creation du Socket

        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2) envoi d'une requête de connexion au serveur:
        
        try:
            connexion.connect( (self.ip, self.port) )
            print "Connexion etablie avec le serveur"
        
        except socket.error:
            print "La connexion a échoué."
            sys.exit()
        
        thR = Reception(connexion)
        thE = Emission(connexion)
        
        thR.start()
        thE.start()
         
         
         
         
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("tentative de connexion au serveur")
        
        try:
            conn.connect( (self.ip, self.port) )
            print ("Connexion etablis avec succes")
        
        except socket.error:
            print ("La liaison du socket a l'adresse choisie a echoue.")
            sys.exit()
            
        return conn
        
        
    def getClient(self):
        liste = list(self.Client)
        return liste

    
if __name__ == '__main__':
    myServer = Server("192.168.0.32", 50000)