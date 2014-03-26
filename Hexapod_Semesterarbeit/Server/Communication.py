'''
Created on 25 mars 2014

@author: Matthieu
'''

import socket, sys, threading
import cmdServos

class Communication(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self, serv, conn):
        '''
        Constructor
        '''
        
        threading.Thread.__init__(self)
        
        self.connexion = conn
        self.serveur   = serv
    
    def run(self):
        
        while 1:    
            """
            lecteur et traitement du message
            """
            
            message = self.connexion.recv(1024)
            
            if message.upper() == "END":
                self.deconnexion() 
            
            """
            renvoie de la reponse
            """
            
            reponse = ""
            
            self.connexion.send(reponse)
                
            
    def deconnexion(self):
        print("connexion termine")
        self.connexion.send("END")
        self.connexion.close()