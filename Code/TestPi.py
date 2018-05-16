import math
from scipy import stats
from Code import PiDecimalCounter

#Les valeurs d'alpha à tester
alphas = [0.001, 0.025, 0.05, 0.1]


def chi2Pi():
    """
    Test du Chi2 sur les decimales de Pi
    """
    countPi = PiDecimalCounter.countDigitFrequency()
    #Il y a 10 chiffre dans la proba de chaque chiffre est de 10%
    proba = [1./10 * 1000000] * 10
    number = len(PiDecimalCounter.getPiDecimalNumber())
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

    for i in range (0, len(proba)):
        ni = proba[i]
        Kr = Kr + (math.pow((ni - probaExp[i]), 2))/probaExp[i]

    df = len(proba) - 1
    critical = stats.chi2.ppf(1 - alpha, df)
    print("La valeur critique est {0} et la valeur théorique est {1}".format(critical, Kr))
    return critical >  Kr

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






