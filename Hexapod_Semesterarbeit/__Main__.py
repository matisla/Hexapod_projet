'''
Created on 31 mars 2014

@author: Matthieu
'''

'''
Created on 27 mars 2014

@author: Matthieu
'''

from Server import Server
from UserInterface import GUI


"""
lancement du serveur
"""

server = Server("localhost", 50000, Debug=True)


"""
Interface graphique
"""

myInterface = GUI(Debug=True)

