'''
Created on 26 mars 2014

@author: Matthieu
'''

import socket, sys, threading
from Communication import *

class Server(threading.Thread):


    def __init__(self, HOST="168.192.0.32", PORT=50000):
        
        threading.Thread.__init__(self)
        
        self.ip   = HOST
        self.port = PORT
        
        self.Client  = {}
        
        self.connexion = self.connexion()
        self.start()
       
    def run(self):
         
        while 1:
                  
            connexion, adresse = self.connexion.accept()
            
            client = Communication(connexion)
            client.start()
            
            nom = "Client%s" %(len(self.Client))
            self.Client[nom] = connexion
                        
            print("")
            print ("%s connecte, adresse IP %s, port %s." %(nom, adresse[0], adresse[1]))
        
            
    def connexion(self):
        
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("lancement du Server")
        
        try:
            mySocket.bind((self.ip, self.port))
            print ("Serveur en route")
        
        except socket.error:
            print ("echec lors du lancement du Server")
            sys.exit()
        
        print("")
        
        mySocket.listen(5)
                
        return mySocket
        
        
    def getClient(self):
        liste = list(self.Client)
        return liste
    
    def shutdown(self):
        self.connexion.close()
    
if __name__ == '__main__':
    myServer = Server("192.168.0.32", 50000)