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
        
        self.ui = None
       
    def connexion(self):
        
        # Creation du Socket

        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2) envoi d'une requete de connexion au serveur:
        self.logger("connexion en cours")
        
        try:
            connexion.connect( (self.ip, self.port) )
            print ("Connexion reussi")
        
        except socket.error:
            print ("echec de la connexion")
            sys.exit()
        
        self.thR = Reception(connexion, self.ui)
        self.thE = Emission(connexion, self.ui)
        
        self.thR.start()
        self.thE.start()

    def deconnexion(self):
        self.thE.sendMsg("end")
    
    def sendMsg(self, message):
        self.listMsg.append(message)
        
    def getClient(self):
        return (self.thE, self.thR)
    
    def setUi(self, GUI):
        self.ui = GUI
    
    def logger(self, message):
        if self.ui is not None:
            self.ui.log(message)
        
        else:
            print(message)
    
if __name__ == '__main__':
    myClient = Client()