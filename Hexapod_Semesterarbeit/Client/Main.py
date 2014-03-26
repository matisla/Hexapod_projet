'''
Created on 24 mars 2014

@author: Matthieu
'''
from User_Interface import *
from Transmission import *

"""
lancer l'interface graphique
"""

ui = User_Interface()

"""
lancer la connexion avec l'hexapod
"""

communication = Transmission(ui)
communication.start()
