'''
Created on 26 mars 2014

@author: Matthieu
'''

import socket, sys, threading
from User_Interface import *

class Transmission(threading.Thread):
    '''
    Permet la communication avec le serveur (hexapod)
    c'est un thread qui lit les messages et les ecrit dans le log du User_Interface
    il a egalement une methode pour envoyer des commandes
    '''
    
    def __init__(self, GUI, HOST='192.168.1.1', PORT=50000):
        
        threading.Thread.__init__(self)
        
        self.ui   = GUI
        self.ip   = HOST
        self.port = PORT
        
        self.connexion = self.connexion()
        self.connexion.send("Bonjour")


    def run(self):
    
        while 1:
            # cycle normal
            
            message = self.connexion.recv(1024)
            
            if message.upper() == "END":
                break
            
            self.ui.log(message)
            

    
    def sendMsg(self, message):
        """
        envoie le message
        """
        self.connexion.send(message)
        
        if message.upper() == "END":
            self.deconnexion()


    def connexion(self):
         
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ui.log("tentative de connexion au serveur")
        
        try:
            conn.connect( (self.ip, self.port) )
            self.ui.log("Connexion etablis avec succes")
        
        except socket.error:
            self.ui.log("La liaison serveur a echoue.")
            sys.exit()

    def deconnexion(self):
        
        self.ui.log("deconnexion")
        self.connexion.close()
    


if __name__ == '__main__':
    mySender = Transmission()