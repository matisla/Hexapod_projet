'''
Created on 26 mars 2014

@author: Matthieu
'''

import socket, sys, threading

from . import Emission, Reception

class Client():


    def __init__(self, HOST="localhost", PORT=50000, gui=None, Debug=True):
        
        self.debug = Debug
        
        self.ip   = HOST
        self.port = PORT
        
        self.ui = gui
       
    def connexion(self):

        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if self.debug is True:
            print("")
            print("connexion en cours")
        
        try:
            connexion.connect( (self.ip, self.port) )
            
            if self.debug is True:
                print("connexion etablie avec le Server")
                print("")
                
            self.logger("Connexion reussi")
            
            self.thR = Reception.Reception(connexion, self.ui)
            self.thE = Emission.Emission(connexion, self.ui)
        
            self.thR.start()
            self.thE.start()
        
            return True
        
        except socket.error as e:
        
            self.logger("echec de la connexion: " + str(e))
            
            return False
        

    def deconnexion(self):
        self.thE.sendMsg("end")
        
        if self.debug is True:
            print("Client: deconnexion en cours ...")
        
    
    def sendMsg(self, message):
        self.thE.sendMsg(message)
        
    def getClient(self):
        return (self.thE, self.thR)
    
    def setUi(self, gui):
        self.thE.setUi(gui)
        self.thR.setUi(gui)
    
    def logger(self, message):
        if self.ui is not None:
            self.ui.log(message)
        
        else:
            if self.debug is True:
                print("")
                print("[Attention]: pas de log attribue")
                
            print(message)
    
if __name__ == '__main__':
    myClient = Client()
    sys.exit()