import time
from Code import PiDecimalCounter

'''
Cette classe permet de généré des nombre aléatoire en utilisant les 1000000 de premières décimales de pi
'''
class RandomGenerator:

    '''
    Initialise la classe
    index est le l'indice dans pi actuellement utilisé
    '''
    def __init__(self):
        self.pi = PiDecimalCounter.getPiDecimalNumber()
        self.a = 3
        self.c = 9
        self.m = 1000000
        self.index = int(time.time()) % self.m



    def random(self):
        x = self.index
        self.index = ((self.a * x) + self.c) % self.m
        return int(self.pi[self.index])
