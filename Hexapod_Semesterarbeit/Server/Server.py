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
        
        self.emetteur  = {}
        self.recepteur = {}
        
        self.numero = 0
        
        self.socket = self.connexion()
       
       
    def run(self):
         
        while 1:
                  
            connexion, adresse = self.socket.accept()
            
            self.numero += 1
            
            th = Communication(connexion)
            th.start()
            
            message = ""
            
            while message == "":
                message = connexion.recv(1024)
            
            if message.upper() == "EMETTEUR":
                self.recepteur["%d" %(self.numero)] = connexion
            if message.upper() == "RECEPTEUR":
                self.emetteur["%d" %(self.numero)]  = connexion
        
            print "Client %s connecte, adresse IP %s, port %s." %("%d" %(self.numero), adresse[0], adresse[1])
        
            connexion.send("Welcome")
            
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
        
        
    def getEmetteur(self):
        liste = list(self.emetteur)
        return liste
    
    def getRecepteur(self):
        liste = list(self.recepteur)
        return liste
    
if __name__ == '__main__':
    pass