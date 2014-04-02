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
        
        self.board = I2CBoard()
        
    def forward(self):
        print("avancer")
    
    def backward(self):
        print("reculer")
        
    def left(self):
        print("aller a gauche")
        
    def right(self):
        print("aller a droite")
        
    def Rleft(self):
        print("tourner a gauche")
        
    def Rright(self):
        print("tourner a droite")    
        
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