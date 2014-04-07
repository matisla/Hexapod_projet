'''
Created on 7 avr. 2014

@author: Matthieu
'''
import sys, os

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_dir)

__all__ = ["Client", "Server"]