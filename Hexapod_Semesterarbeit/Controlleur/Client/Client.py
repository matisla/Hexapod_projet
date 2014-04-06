'''
Created on 26 mars 2014

@author: Matthieu
'''

import socket

from Emission import Emission
from Reception import Reception


class Client():
    """
    classe qui lance la connexion avec un Thread Emission et un Thread Reception
    peut aussi envoyer des messages grace a la commande sendMsg()
    """

    def __init__(self, HOST="localhost", PORT=50000, gui=None, Debug=True):
        
        self.debug = Debug
        
        self.ip   = HOST
        self.port = PORT
        
        self.ui  = gui
        self.thE = None
        self.thR = None
       
    def connexion(self):
        """
        lance la connexion du client
        return True or False suivant la reussite ou l'echec
        """
        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if self.debug is True:
            print("[Client]: Client        >> connexion au Server en cours")
        
        try:
            connexion.connect( (self.ip, self.port) )
            
            if self.debug is True:
                print("[Client]: Client        >> connexion au Server reussi")
            
            self.thR = Reception(connexion, self.ui, Debug=self.debug)
            self.thE = Emission(connexion, self.ui, Debug=self.debug)
        
            self.thR.start()
            self.thE.start()
        
            return True
        
        except socket.error as e:
            
            if self.debug is True:
                print("[Client]: Client        >> [ERROR] connexion impossible")
            self.logger(str(e))
            
            return False
        

    def deconnexion(self):
        self.thE.sendMsg("end")
        
        if self.debug is True:
            print("[Client]: Client        >> fin de la communication")
        
    
    def sendMsg(self, message):
        self.thE.sendMsg(message)
        
    def getClient(self):
        return (self.thE, self.thR)
    
    def setUi(self, gui):
        self.ui = gui
        
        if self.thE is not None:
            self.thE.setUi(gui)
        
        if self.thR is not None:
            self.thR.setUi(gui)
        
        
    def logger(self, message):
        if self.ui is not None:
            self.ui.log(message)
        
        else:
            if self.debug is True:
                print("[Client]: Client        >> [Attention] pas de log attribue")
                
            print("                           " + message)
    
if __name__ == '__main__':
    myClient = Client(Debug=True)
    myClient.connexion()