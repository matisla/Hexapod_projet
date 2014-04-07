'''
Created on 26 mars 2014

@author: Matthieu
'''

import socket, threading

from Communication import Communication

class Server(threading.Thread):
    '''
    classe permettant de generer un serveur
    '''


    def __init__(self, HOST="localhost", PORT=50000, Debug=False):
        '''
        Host, port: donner l'ip et le port pour la connexion du serveur
        Debug: affiche les messages de debugging dans la console
        '''
        
        self.debug = Debug
        self.actif = True
        
        threading.Thread.__init__(self)
        
        self.setName("Server")
        
        self.ip   = HOST
        self.port = PORT
        
        self.Client  = {}
        
        self.conn = self.connexion()
        
        if self.conn is not False:
            self.start()

       
    def run(self):
         
        if self.debug is True:
            print("[Server]: Server        >> en attente de connexion ...")
            
            
        while self.actif is True:    
                  
            connexion, adresse = self.conn.accept()
            
            nom = "Client%s" %(len(self.Client))
            
            if self.debug is True:
                print("[Server]: Server        >> %s connecte, adresse IP %s, port %s" %(nom, adresse[0], adresse[1]))
            
            client = Communication(self, connexion, Debug=self.debug)
            client.setName(nom)
            
            self.Client[nom] = connexion
            
            client.start()
            
            
            
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
                print("[Server]: Server        >> [ERROR] connexion impossible")
                print("                           " + str(e))
            else:
                print(str(e))
                
            return False
        
        
    def getClient(self):
        liste = list(self.Client)
        return liste
    
    def delClient(self, nom):
        del self.Client[nom]
    
    def shutdown(self):
        if self.debug is True:
            print("[Server]: Server        >> Shutdown du Server")
            
        self.actif = False
            
if __name__ == '__main__':
    myServer = Server(Debug=True)