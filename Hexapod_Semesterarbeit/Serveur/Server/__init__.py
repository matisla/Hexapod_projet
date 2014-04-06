
import os, sys

# liste l'ensemble des modules du package
__all__ = ["Server", "Communication"]


file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_dir)