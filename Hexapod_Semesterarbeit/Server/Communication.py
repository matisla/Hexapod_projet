'''
Created on 25 mars 2014

@author: Matthieu
'''

import socket, sys

class Communication():
    '''
    classdocs
    '''


    def __init__(self, HOST='192.168.1.1', PORT=50000):
        '''
        Constructor
        '''
        
        self.ip   = HOST
        self.port = PORT
        
        self.mySocket  = self.connexion()
        self.connexion = self.ecoute()
        self.start()
        
    def connexion(self):
        
        Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.Sock.bind( (self.ip, self.port) )
            print "Connexion reussi !"
        
        except:
            print("la liaison du socket a echoue")
            sys.exit()
        
        return Sock
    
    def deconnexion(self):
        print("connexion termine")
        self.connexion.send("END")
        self.connexion.close()
         
        
    def ecoute(self):
        
        print("attente d'une requete")
        while 1:
            
            self.mySocket.listen(5)
            
            conn, adresse = self.mySocket.accept()
            print "Client connecte, adresse IP %s, port %s" % (adresse[0], adresse[1])
            
            return conn
            
            
    def sendMsg(self, message):
        self.connexion.send(message)
            
    def readMsg(self):
        message = self.connexion.recv(1024)
        return message
            
            