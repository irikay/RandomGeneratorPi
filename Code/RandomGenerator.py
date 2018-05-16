import time
from Code import PiDecimalCounter

'''
Cette classe permet de généré des nombre aléatoire en utilisant les 1000000 de premières décimales de pi
'''
class RandomGenerator:
    def __init__(self):
        """
        Initialise la classe
        index est le l'indice dans pi actuellement utilisé
        """
        self.pi = PiDecimalCounter.getPiDecimalNumber()
        self.a = 3
        self.c = 9
        self.m = 1000000
        self.index = int(time.time()) % self.m



    def random(self, decimals = 10):
        """
        Génére un nombre aléatoire et change la valeure de l'index

        :param decimals: le nombre de décimale du nombre généré (16 max car c'est un float)
        :return: Un nombre aléatoire
        """
        random = "0."
        for i in range(0, decimals):
            self.index = ((self.a * self.index) + self.c) % self.m
            random += self.pi[self.index]
        return float(random)
