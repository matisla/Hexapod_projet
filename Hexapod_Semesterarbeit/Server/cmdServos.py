'''
Created on 19 mars 2014

@author: Matthieu
'''

class cmdServos(object):
    '''
    les differentes commandes permettants de faire bouger les servos.
    Ces differentes commandes sont envoye par le lien I2C au controleur.
    
    '''


    def __init__(self, nom, adresse):
        '''
        Constructor
        adresse: adresse du controlleur en I2C
        '''
        self.addr = adresse
        self.name = nom
        self.getaddr
        
    def getaddr(self):
        print("Caracteristique du Controlleur:")
        print("nom:     %s"   %(self.name))
        print("adresse: 0x%X" %(self.addr))
        
if __name__ == '__main__':
    test = cmdServos("gauche", 0x10)
    test.getaddr()