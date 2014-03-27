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


    def __init__(self, conn):
        '''
        Constructor
        '''
        
        threading.Thread.__init__(self)
        
        self.connexion = conn
    
    
    def run(self):
        
        while 1:    
            """
            lecteur et traitement du message
            """
            
            message = self.connexion.recv(1024)
            message = message.decode()
            
            if message.upper() == "END":
                self.deconnexion() 
                
            print("message recu Communication: " + message)
            
            """
            renvoie de la reponse
            """
            
            reponse = "message recu"
            
            self.connexion.send(reponse)
                
        self.deconnexion()
        
    def deconnexion(self):
        self.connexion.close()
        
if __name__ == '__main__':
    print("lancer le serveur SVP")