'''
Created on 31 mars 2014

@author: Matthieu
'''

'''
Created on 27 mars 2014

@author: Matthieu
'''
import sys

from Client import Client
from Server import Server
from UserInterface import GUI

"""
Interface graphique
"""

myInterface = GUI.GUI()


"""
Connexion
"""

host="192.168.211.195"
port=50000

server = Server.Server(host, port)

client = Client.Client(host, port)

client.connexion()


"""
lien entre connexion et partie Graphique
"""

client.setUi(myInterface)


"""
Quitter l'application
"""


client.deconnexion()

sys.exit()