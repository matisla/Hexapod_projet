'''
Created on 6 avr. 2014

@author: Matthieu

Main Server

'''

"""
#importation dans le path du dossier actuelle si il n'y est pas

import os, sys

projet_dir = os.path.dirname(os.path.abspath(__file__))

if projet_dir not in sys.path:
    sys.path.append(projet_dir)
"""

from Server import Server
    
myServer = Server(Debug=True)
