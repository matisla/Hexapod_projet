
# liste l'ensemble des modules du package
__all__ = ["Server", "Communication"]

import os, sys

projet_dir = os.path.dirname(os.path.abspath(__file__))

if projet_dir not in sys.path:
    sys.path.append(projet_dir)