'''
Created on 24 mars 2014

@author: Matthieu
'''

import threading


class Reception(threading.Thread):
    
    """
    Thread Client qui permet de receptions les information qui vienne de l'hexapod
    
    """
    
    def __init__(self, conn,  gui=None, Debug=True):

        self.debug = Debug
        self.message = []
        
        threading.Thread.__init__(self)                
        self.setName("Reception")
        
        self.connexion = conn
        
        self.ui = gui
    
    def run(self):
        
        while 1:
            # cycle normal
            try:
                message = self.connexion.recv(1024)
                message = message.decode()
            
            except:
                print("erreur lors de la lecture de la reponse")
                
            if self.debug is True:
                print("[Client]: Reception     >> message recu: " + message)
                    
            if message.upper() == "END":
                if self.debug is True:
                    print("[Client]: Reception     >> fin de la communication")    
                break
            
            elif message.upper() == "BEGIN":
                if self.debug is True:
                    print("[Client]: Reception     >> Debut de la communication")    
                self.logger("Debut de la communication avec le Server")
                
            else:
                self.logger(message)
        
        
        self.connexion.close()
    
    
    
    def logger(self, message=""):
        
        if message != "":
            self.message.append(message)
        
        if self.ui is not None:
            for msg in self.message:
                self.ui.log(msg)
                self.message.remove(msg)
            
        else:
            if self.debug is True:
                print("[Client]: Reception     >> [Attention] pas de log attribue")
            
                print("[Client]: Reception     >> message en attente: ")
                for msg in self.message:
                    print("                           " + msg)
            
    def setUi(self, gui):
        self.ui = gui
        self.logger()
        
        if self.debug is True:
            print("[Client]: Reception     >> Thread Reception - Interface Graphique PRET")

if __name__ == '__main__':
    print("lancer le Client SVP")