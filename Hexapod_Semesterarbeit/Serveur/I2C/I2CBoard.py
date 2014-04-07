'''
Created on 1 avr. 2014

@author: Matthieu
'''
#from smbus import *

class I2CBoard():
    '''
    classdocs
    '''


    def __init__(self, adresse=None, Debug=False):
        '''
        adresse: adresse du controlleur en I2C
        '''
        
        self.debug = Debug
#        self.bus  = smbus.SMBus(1)
        
        self.addr = None
        
        if self.debug is True:
            print("[I2C]:    I2CBoard      >> pret a transmettre les commandes")
        
        
    def scannBoard(self):
        
        if self.debug is True:
            for adresse in self.addr:
                print("[I2C]:    I2CBoard      >>Board a l'adresse 0x%02X" %(adresse))
    
    def read(self):
        """
        try:
            lecture = self.bus.read_byte_data(self.address, reg)
            if self.debug:
            
        tmp = bus.read_word_data(address , 0 )
        """
    
    def bonjours(self):
        print("bonjours de I2CBoard")
        
        
if __name__ == '__main__':
    addr = 0
    
    try:
        bus = I2CBoard(adresse=addr)
        print("[I2C]:    I2CBoard      >> Connexion a l'adresse 0x%02X reussi" % (addr))
    except:
        print("[I2C]:    I2CBoard      >> Connexion a l'adresse 0x%02X a echoue" % (addr))