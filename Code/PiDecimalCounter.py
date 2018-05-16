from random import Random

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
    test = RandomGenerator.RandomGenerator()
    n = 0
    for i in range(0,0):
        n += test.random(1)
    print(n)
    '''
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    test = RandomGenerator.RandomGenerator()
    for i in range(0,1000000):
        number = int(test.random())
        count[number] = count[number] + 1
    for i in range(0, len(count)):
        print(count[i])
    '''