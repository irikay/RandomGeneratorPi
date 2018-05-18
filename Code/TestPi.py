import math
import random
from scipy import stats
from Code import PiDecimalCounter
from Code import RandomGenerator

#Les valeurs d'alpha à tester
alphas = [0.001, 0.025, 0.05]



def chi2RandomPython():
    """
    Test du Chi2 sur le générateur aléatoire de python
    """
    number = 1000000
    total = 0.0
    proba = [1. / 10 * number] * 10
    count = [0] * 10
    for i in range(0, number):
        n = float(random.random()) * 10
        total += n
        index = int(n)
        count[index] = count[index] + 1
    for alpha in alphas:
        print("Test du chi2 pour le générateur aléatoire de python avec alpha = {0}".format(alpha))
        if chi2(count, proba, alpha):
            print("On a donc que le test du chi2 réussi")
        else:
            print("On a donc que le test à échouer")
        print()

def chi2RandomPi():
    """
    Test du Chi2 sur le générateur aléatoire de python
    """
    number = 1000000
    proba = [1. / 10 * number] * 10
    count = [0] * 10
    rand = RandomGenerator.RandomGenerator()
    for i in range(0, number):
        n = float(rand.random())
        index = int(n*10)
        count[index] = count[index] + 1
    for alpha in alphas:
        print("Test du chi2 de notre générateur aléatoire avec alpha = {0}".format(alpha))
        if chi2(count, proba, alpha):
            print("On a donc que le test du chi2 réussi pour les intervalle de nombre")
        else:
            print("On a donc que le test à échouer")
        print()


def chi2Pi():
    """
    Test du Chi2 sur les decimales de Pi
    """
    countPi = PiDecimalCounter.countDigitFrequency()
    #Il y a 10 chiffre dans la proba de chaque chiffre est de 10%
    proba = [1./10 * 1000000] * 10
    for alpha in alphas:
        print("Test du chi2 pour les décimales de Pi avec alpha = {0}".format(alpha))
        if chi2(countPi, proba, alpha):
            print("On a donc que le test du chi2 réussi")
        else:
            print("On a donc que le test à échouer")
        print()

def chi2(proba, probaExp, alpha):
    """
    Test du Chi2

    :param proba: les probabilités qu'on veut comparé
    :param probaExp: les probabiulité attendue théoriquement
    :param alpha: la valeur d'alpha
    :return: vrai si on accepte l'hypothèse, faux sinon
    """
    Kr = 0

    for i in range(0, len(proba)):
        ni = proba[i]
        Kr = Kr + (math.pow((ni - probaExp[i]), 2))/probaExp[i]

    df = len(proba) - 1
    critical = stats.chi2.ppf(1 - alpha, df)
    print("La valeur critique est {0} et la valeur théorique est {1}".format(critical, Kr))
    return critical > Kr

def gapRandomPython():
    """
    Test du gap sur le générateur aléatoire de python
    """
    number = 1000
    total = ""
    #On sauvegarde tout les nombre généré les uns à la suite des autres sans le "0."
    for i in range(0, number):
        s = random.random()
        r = repr(s)
        if 'e' in r:  # Detecte la notation scientifique, voir https://stackoverflow.com/questions/38847690/convert-float-to-string-without-scientific-notation-and-false-precisionhttps://stackoverflow.com/questions/38847690/convert-float-to-string-without-scientific-notation-and-false-precision
            digits, exp = r.split('e')
            digits = digits.replace('.', '').replace('-', '')
            exp = int(exp)
            zero_padding = '0' * (abs(int(exp)) - 1)
            if exp > 0:
                r = '{}{}.0'.format(digits, zero_padding)
            else:
                r = '0.{}{}'.format(zero_padding, digits)
            s = r
        else:
            s = str(s)
        total += s[2:]
    print(total)
    numberOfClass = 60
    tests = [False] * 10
    for alpha in alphas:
        print("Test du Gap pour le générateur de python avec alpha = {0}".format(alpha))
        for i in range(0, len(tests)):
            print("Pour la décimale {0} on a donc que:".format(i))
            if gapTest(total, i, numberOfClass, alpha):
                print("Le test du gap est donc réussi")
            else:
                print("Le test du gap à donc échouer")

def gapRandomPi():
    """
    Test du gap sur notre générateur aléatoire
    """
    number = 1000
    total = ""
    rand = RandomGenerator.RandomGenerator()
    #On sauvegarde tout les nombre généré les uns à la suite des autres sans le "0."
    for i in range(0, number):
        s = rand.random()
        r = repr(s)
        if 'e' in r:  # Detecte la notation scientifique, voir https://stackoverflow.com/questions/38847690/convert-float-to-string-without-scientific-notation-and-false-precisionhttps://stackoverflow.com/questions/38847690/convert-float-to-string-without-scientific-notation-and-false-precision
            digits, exp = r.split('e')
            digits = digits.replace('.', '').replace('-', '')
            exp = int(exp)
            zero_padding = '0' * (abs(int(exp)) - 1)
            if exp > 0:
                r = '{}{}.0'.format(digits, zero_padding)
            else:
                r = '0.{}{}'.format(zero_padding, digits)
            s = r
        else:
            s = str(s)
        total += s[2:]
    numberOfClass = 60
    tests = [False] * 10
    for alpha in alphas:
        #print("Test du Gap pour les décimales de Pi avec alpha = {0}".format(alpha))
        for i in range(0, len(tests)):
            print("Pour la décimale {0} on a donc que:".format(i))
            if gapTest(total, i, numberOfClass, alpha):
                a = 0
                print("Le test du gap est donc réussi")
            else:
                a =1
                print("Le test du gap à donc échouer")

def gapPi():
    """
    Test du gap sur les décimal de pi
    """
    pi = PiDecimalCounter.getPiDecimalNumber()
    numberOfClass = 60
    tests = [False] * 10
    for alpha in alphas:
        print("Test du Gap pour les décimales de Pi avec alpha = {0}".format(alpha))
        for i in range(0, len(tests)):
            print("Pour la décimale {0} on a donc que:".format(i))
            if gapTest(pi, i, numberOfClass, alpha):
                print("Le test du gap est donc réussi")
            else:
                print("Le test du gap à donc échouer")


def gapTest(sequence, number, numberOfClasses, alpha):
    """
    Test du gap

    :param sequence: la sequence de nombre a analyser
    :param number: le nombre qu'on va marqué
    :param numberOfClasses: la taille maximal des trous qu'on va considéré entre 2 nombres marqué
    :param alpha: la valeur d'alpha pour le test de chi2
    :return: vrai si on accepte l'hypothèse, faux sinon
    """
    classes = [0] * numberOfClasses
    gap = 0
    seen = False
    for n in range(0, len(sequence)):
        #print(sequence[n])
        num = int(sequence[n])
        if num == number:
            if seen and gap < numberOfClasses :
                classes[gap] = classes[gap] + 1
                gap = 0
            else:
                gap = 0
                seen = True
        else:
            gap += 1

    probaTheorical = [0] * numberOfClasses
    for n in range(0, numberOfClasses):
        probaTheorical[n] = getTheoricalProbaGap(n) * len(sequence)/10.
    return chi2(classes, probaTheorical, alpha)

def getTheoricalProbaGap(gap):
    """
    Nous donne la valeur théorique pour un trou d'une certaine taille

    :param gap: la taille du trou
    :return: la valeur théorique
    """
    return (1.0/10)* math.pow(9.0/10, gap)






