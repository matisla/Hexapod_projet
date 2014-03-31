'''
Created on 26 mars 2014

@author: Matthieu
'''

import socket, sys, threading

from . import Emission, Reception

class Client():


    def __init__(self, HOST="168.192.0.32", PORT=50000, gui=None):
        
        self.ip   = HOST
        self.port = PORT
        
        self.ui = gui
       
    def connexion(self):
        
        # Creation du Socket

        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2) envoi d'une requete de connexion au serveur:
        self.logger("connexion en cours")
        
        try:
            connexion.connect( (self.ip, self.port) )
            self.logger("Connexion reussi")
        
        except socket.error as e:
            self.logger("echec de la connexion")
            self.logger(e)
            sys.exit()
        
        self.thR = Reception.Reception(connexion, self.ui)
        self.thE = Emission.Emission(connexion, self.ui)
        
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
        self.thE.setUi(GUI)
        self.thR.setUi(GUI)
    
    def logger(self, message):
        if self.ui is not None:
            self.ui.log(message)
        
        else:
            print(message)
    
if __name__ == '__main__':
    myClient = Client()