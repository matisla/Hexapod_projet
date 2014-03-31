'''
Created on 25 mars 2014

@author: Matthieu
'''

import socket, sys, threading

from .cmdServos import *


class Communication(threading.Thread):
    '''
    Thread cote serveur permettant la communication avec UN Client
    '''


    def __init__(self, conn, Debug=True):
        '''
        Debug = True permet d'afficher les messages dans la console
        '''
        
        threading.Thread.__init__(self)
        
        self.debug = Debug
            
        self.connexion = conn
    
    
    def run(self):
        
        if self.debug is True:
            print("")
            print("pret a recevoir les commandes !")
            print("")
            
        while 1:    
            """
            lecteur et traitement du message
            """
            
            message = self.connexion.recv(1024)
            message = message.decode()
            
            if message.upper() == "END":
                self.connexion.send(message.encode())
                break
            
            else:
                print("recepteur Server message: "+ message)
            
                """
                renvoie de la reponse
                """
                
                reponse = "message recu"
                self.connexion.send(reponse.encode())
                
        
if __name__ == '__main__':
    print("lancer le serveur SVP")