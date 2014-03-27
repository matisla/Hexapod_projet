'''
Created on 24 mars 2014

@author: Matthieu
'''
from User_Interface import *
import Emission
import Reception

"""
lancer l'interface graphique
"""

#ui = User_Interface()

"""
lancer la connexion avec l'hexapod
"""
thE = Emission()
thR = Reception()

thE.start()
thR.start()
