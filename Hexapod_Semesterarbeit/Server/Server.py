'''
Created on 26 mars 2014

@author: Matthieu
'''

import socket, sys, threading
import Communication

class Server(threading.Thread):


    def __init__(self, HOST="168.192.1.1", PORT=50000):
        
        threading.Thread.__init__(self)
        
        self.ip   = HOST
        self.port = PORT
        
        self.Client  = {}
        
        self.socket = self.connexion()
       
       
    def run(self):
         
        while 1:
                  
            connexion, adresse = self.socket.accept()
            
            th = Communication(self, connexion)
            th.start()
            
            message = connexion.recv(1024)
            
            while message.upper() != "BONJOUR":
                message = connexion.recv(1024)
            
            nom = "Client%s" %(len(self.Client))
            self.Client[nom] = connexion
        
            print "%s connecte, adresse IP %s, port %s." %(nom, adresse[0], adresse[1])
        
            connexion.send("Bonjour")
            
    def connexion(self):
        
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("connexion avec le socket")
        
        try:
            mySocket.bind((self.ip, self.port))
            print "Connexion etablis avec succes"
        
        except socket.error:
            print "La liaison du socket a l'adresse choisie a echoue."
            sys.exit()
        
        mySocket.listen(5)
                
        return mySocket
        
        
    def getClient(self):
        liste = list(self.Client)
        return liste

    
if __name__ == '__main__':
    pass