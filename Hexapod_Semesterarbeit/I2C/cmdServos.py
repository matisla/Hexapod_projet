'''
Created on 19 mars 2014

@author: Matthieu
'''

from I2CBoard import I2CBoard

class cmdServos(object):
    '''
    les differentes commandes permettants de faire bouger les servos.
    Ces differentes commandes sont envoye par le lien I2C au controleur.
    
    '''


    def __init__(self, Debug=False):
        
        self.debug  = Debug
        self.boardG = I2CBoard(adresse=0x0)
        self.boardD = I2CBoard(adresse=0x0)
        
    def cmd(self, message):
        
        if self.debug is True:
            print("[I2C]: cmdServos        >> commande recu: " + message)
               
        if message == "DECONNEXION":
            print("deconnexion de la communication I2C")
            
        elif message == "FW":
            
            print("avancer")   
            reponse = True   
        
        elif message == "BW":
            
            print("reculer")
            reponse = True
            
        elif message == "LE":
            
            print("Gauche")
            reponse = True
            
        elif message == "RI":
            
            print("Droite")
            reponse = True
            
        elif message == "RL":
            
            print("Rotation Gauche")
            reponse = True
            
        elif message == "RR":
            
            print("Rotation Droite")
            reponse = True
            
        else:
            print("[ERROR] commande inconnu !")
            reponse = False
            
        return reponse
    
    
    def servos(self, numero, valeur):
        """
        controle manuelle du servos XYZ
        
        X: gauche (0), droite (1)
        Y: nummero de la patte (1 etant l'avant)
        Z: nummero du servo (1 etant l'interieur)
        """
            
                    
if __name__ == '__main__':
    test = cmdServos("gauche", 0x10)
    test.getaddr()