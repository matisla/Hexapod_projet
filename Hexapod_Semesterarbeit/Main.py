'''
Created on 24 mars 2014

@author: Matthieu
'''

from GUI import *
from Emission import *
from Reception import *

"""
lancer la connexion avec l'hexapod
Emission pour envoyer les commandes
Reception pour recevoir le retour des commandes
"""

Emetteur  = Emission()

Recepteur = Reception()
Recepteur.start()

"""
lancer l'interface graphique
"""

ui = User_Interface()
