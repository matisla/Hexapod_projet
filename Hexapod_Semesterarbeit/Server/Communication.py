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
            print("[Server]: Communication >> pret a recevoir les commandes")
        
        while 1:
            message = self.connexion.recv(1024)
            message = message.decode()
            message = message.upper()
            
            if message == "BEGIN":
                self.connexion.send(message.encode())
                    
                if self.debug is True:
                    print("[Server]: Communication >> Debut de la communication")
                    
                break   
        
        while 1:    
            """
            lecteur des commandes
            """
            
            message = self.connexion.recv(1024)
            message = message.decode()
            message = message.upper()
            
            reponse = message
            
            if self.debug is True:
                print("[Server]: Communication >> message recu: " + message)
            
            """
            traitement des commandes
            """
            
            if message == "END":
                self.connexion.send(message.encode())
                
                if self.debug is True:
                    print("[Server]: Communication >> fin de la communication")
                break
            
                    
            elif message == "FW":
                reponse = "en Avant !"
            
            elif message == "BW":
                reponse = "en Arriere !"
            
            elif message == "LE":
                reponse = "a Gauche !"
                
            elif message == "RI":
                reponse = "a Droite !"
            
            elif message == "RL":
                reponse = "Tourner a Gauche !"
            
            elif message == "RR":
                reponse = "Tourner a Droite !"
                
            else:
                if self.debug is True:
                    print("[Server]: Communication >> [ERROR] commande inconnue")
                
                reponse = ("[ERROR]: commande inconnu !")
            
                
            """
            renvoie de la reponse
            """
            
            if self.debug is True:
                print("[Server]: Communication >> message rendu: " + reponse)
                
            self.connexion.send(reponse.encode())
                
        
if __name__ == '__main__':
    print("lancer le serveur SVP")