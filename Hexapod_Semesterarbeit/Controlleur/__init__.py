'''
Created on 6 avr. 2014

@author: Matthieu
'''

import os, sys

projet_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(projet_dir)

__all__ =["Client", "UserInterface"]