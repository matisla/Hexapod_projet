
# liste l'ensemble des modules du package
__all__ = ["UserInterface", "Receiver", "Sender"]

import os, sys

for x in sys.path:
    print(x)

projet_dir = os.path.dirname(os.path.abspath(__file__))

if projet_dir not in sys.path:
    sys.path.append(projet_dir)
    print("ajoute dans le path du chemin")