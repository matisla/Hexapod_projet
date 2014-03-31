'''
Created on 26 mars 2014

@author: Matthieu
'''

import socket, threading

from .Communication import *


class Server(threading.Thread):


    def __init__(self, HOST="localhost", PORT=50000, Debug=True):
        
        self.debug = Debug
        
        threading.Thread.__init__(self)
        
        self.setName("Server")
        
        self.ip   = HOST
        self.port = PORT
        
        self.Client  = {}
        
        self.conn = self.connexion()
        
        if self.conn != False:
            self.start()

       
    def run(self):
         
        while 1:
                  
            connexion, adresse = self.conn.accept()
            
            nom = "Client%s" %(len(self.Client))
            
            client = Communication(connexion, Debug=self.debug)
            client.setName(nom)
            
            self.Client[nom] = connexion
            
            client.start()
            
            if self.debug is True:
                print("[Server]: Server        >> %s connecte, adresse IP %s, port %s" %(nom, adresse[0], adresse[1]))
                
    def connexion(self):
        
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if self.debug is True:
            print("[Server]: Server        >> lancement du server")
        
        try:
            mySocket.bind((self.ip, self.port))
            
            if self.debug is True:
                print("[Server]: Server        >> Server operationnel")
            
            mySocket.listen(5)
            return mySocket
    
        except socket.error as e:

            if self.debug is True:
                print("[Server]: Server        >> Erreur de connexion")
            print(str(e))
            
            return False
        
        
    def getClient(self):
        liste = list(self.Client)
        return liste
    
    
    def shutdown(self):
        self.connexion.close()
    
        if self.debug is True:
            print("[Server]: Server        >> Shutdown du Server")
            
if __name__ == '__main__':
    myServer = Server()