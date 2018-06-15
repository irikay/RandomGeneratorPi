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
        self.m = 1000000
        #diviseur premier de m est 2 et 5, et 4 divise m, donc b multiple de 2,4 et 5
        # et b = a-1 , on dis b = 40, donc on a, a = 41
        self.a = 41

        #c est premier avec m, donc on chosit parmit (3, 7, 9, 11, 13, ...)
        self.c = 11

        #index de départ, choisit en fonction de l'heure actuelle
        self.index = int(time.time()) % self.m



    def random(self, decimals = 16):
        """
        Génére un nombre aléatoire et change la valeure de l'index

        :param decimals: le nombre de décimale du nombre généré (16 max car c'est un float)
        :return: Un nombre aléatoire
        """
        random = "0."
        self.index = ((self.a * self.index) + self.c) % self.m
        random += self.pi[self.index:self.index+decimals]
        return float(random)
