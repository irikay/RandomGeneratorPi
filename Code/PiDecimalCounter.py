import random

from Code import TestPi
from Code import RandomGenerator

def countDigitFrequency():
    """
    Compte le nombre de 0,1,2,3,... dans les décimale de Pi et les place dans une liste
    Le nombre d'occurence du i ème chiffre se trouve dans la i ème position dans la liste retourner

    :return: la liste
    """
    pi = getPiDecimalNumber()
    count = [0,0,0,0,0,0,0,0,0,0]
    for number in pi:
        number = int(number)
        count[number] = count[number] + 1
    return count


def getPiDecimalNumber():
    """
    :return:  un string avec toutes les decimales de pi
    """
    pi_f = open("../Files/pi.txt", "r")
    pi = ""
    for line in pi_f:
        pi += line.rstrip('\r \n')
    # On enleve le '3.14' de pi
    return pi[2:]

if __name__ == '__main__':
    #Test Chi2 sur les decimales de Pi
    TestPi.chi2Pi()
    print()

    #Test du gap sur les decimales de Pi
    TestPi.gapPi()
    print()

    # Test du Poker sur les decimales de Pi
    TestPi.pokerPi()
    print()

    number = 20
    # Test du Chi2 pour le générateur aléatoire de python
    ktot = 0
    for i in range(0, number):
        ktot += TestPi.chi2RandomPython()
    #Kn moyen
    print(ktot / number)
    print()

    # Test du Chi2 pour notre générateur aléatoire
    ktot2 = 0
    for i in range(0, number):
        ktot2 += TestPi.chi2RandomPi()
    #Kn moyen
    print(ktot2 / number)
    print()


    # Test du gap pour le générateur aléatoire de python
    pourcentage = 0
    GKtot1 = 0.0
    for i in range(0,number):
        test = TestPi.gapRandomPython()
        pourcentage += test[0]
        GKtot1 += test[1]
    #Pourcentage de test réussi
    print(pourcentage/number)
    #Kn moyen
    print(GKtot1/number)

    # Test du gap pour notre générateur aléatoire
    pourcentage2 = 0
    GKtot2 = 0.0
    for i in range(0, number):
        test = TestPi.gapRandomPi()
        pourcentage2 += test[0]
        GKtot2 += test[1]
    #Pourcentage de test réussi
    print(pourcentage2 / number)
    #Kn moyen
    print(GKtot2 / number)
    print()

    # Test du Poker pour le générateur aléatoire de python
    ktot = 0
    for i in range(0, number):
        ktot += TestPi.pokerRandomPython()
    # Kn moyen
    print(ktot / number)
    print()

    # Test du Poker pour notre générateur aléatoire
    ktot2 = 0
    for i in range(0, number):
        ktot2 += TestPi.pokerRandomPi()
    # Kn moyen
    print(ktot2 / number)
    print()