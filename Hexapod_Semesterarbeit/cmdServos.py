'''
Created on 19 mars 2014

@author: Matthieu
'''

class cmdServos(object):
    '''
    les differentes commandes permettants de faire bouger les servos.
    Ces differentes commandes sont envoye par le lien I2C au controleur.
    
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        