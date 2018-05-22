import math
import random
from scipy import stats
from Code import PiDecimalCounter
from Code import RandomGenerator

#Les valeurs d'alpha à tester
alphas = [0.001,0.025,0.05]



def chi2RandomPython():
    """
    Test du Chi2 sur le générateur aléatoire de python
    :return un tuple où le premier élément est un boolean qui indique si le test est réussi, et le 2ième élément est la valeur du Kn
    """
    number = 1000000
    proba = [1. / 10 * number] * 10
    count = [0] * 10
    for i in range(0, number):
        n = random.random() * 10
        index = int(n)
        count[index] = count[index] + 1
    test = 0
    for alpha in alphas:
        print("Test du chi2 pour le générateur aléatoire de python avec alpha = {0}".format(alpha))
        test = chi2(count, proba, alpha)
        if test[0]:
            print("On a donc que le test du chi2 réussi")
        else:
            print("On a donc que le test à échouer")
        print()
    return test[1]

def chi2RandomPi():
    """
    Test du Chi2 sur le générateur aléatoire de python

    :return un tuple où le premier élément est un boolean qui indique si le test est réussi, et le 2ième élément est la valeur du Kn
    """
    number = 1000000
    proba = [1. / 10 * number] * 10
    count = [0] * 10
    rand = RandomGenerator.RandomGenerator()
    for i in range(0, number):
        n = rand.random() * 10
        index = int(n)
        count[index] = count[index] + 1
    test = 0
    for alpha in alphas:
        print("Test du chi2 de notre générateur aléatoire avec alpha = {0}".format(alpha))
        test = chi2(count, proba, alpha)
        if test[0]:
            print("On a donc que le test du chi2 réussi")
        else:
            print("On a donc que le test à échouer")
        print()
    return test[1]


def chi2Pi():
    """
    Test du Chi2 sur les decimales de Pi
    """
    countPi = PiDecimalCounter.countDigitFrequency()
    #Il y a 10 chiffre dans la proba de chaque chiffre est de 10%
    proba = [1./10 * 1000000] * 10
    for alpha in alphas:
        print("Test du chi2 pour les décimales de Pi avec alpha = {0}".format(alpha))
        if chi2(countPi, proba, alpha)[0]:
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
    :return un tuple où le premier élément est un boolean qui indique si le test est réussi, et le 2ième élément est la valeur du Kn
    """
    Kr = 0

    for i in range(0, len(proba)):
        ni = proba[i]
        Kr = Kr + (math.pow((ni - probaExp[i]), 2))/probaExp[i]

    df = len(proba) - 1
    critical = stats.chi2.ppf(1 - alpha, df)
    print("La valeur critique est {0} et la valeur expérimentale est de {1}".format(critical, Kr))
    return ((critical > Kr), Kr)

def gapRandomPython():
    """
    Test du gap sur le générateur aléatoire de python

    :return: un tuble, (le pourcentage de test réussi, la moyenne des Kr de tout les test)
    """
    number = 100000
    total = ""
    #On sauvegarde le premier chiffre après la virgule on a 10 intervalles de 0.0 à 0.1, de 0.1 à 0.2, etc
    for i in range(0, number):
        s = str(random.random())
        total += s[2]
    numberOfClass = 55
    tests = [False] * 10
    passed = 0
    tot = 0
    Kr = 0.0
    for alpha in alphas:
        print("Test du Gap pour le générateur de python avec alpha = {0}".format(alpha))
        for i in range(0, len(tests)):
            tot += 1
            print("Pour la décimale {0} on a donc que:".format(i))
            test = gapTest(total, i, numberOfClass, alpha)
            Kr += test[1]
            if test[0]:
                passed += 1
                print("Le test du gap est donc réussi")
            else:
                print("Le test du gap à donc échouer")
    print("Le nombre de test réussi est de {0} sur {1} soit un pourcentage de {2}".format(passed, tot, ((passed)/tot)*100))
    return (((passed) / tot) * 100, Kr/tot)

def gapRandomPi():
    """
    Test du gap sur notre générateur aléatoire

    :return: un tuble, (le pourcentage de test réussi, la moyenne des Kr de tout les test)
    """
    number = 100000
    total = ""
    rand = RandomGenerator.RandomGenerator()
    # On sauvegarde le premier chiffre après la virgule on a 10 intervalles de 0.0 à 0.1, de 0.1 à 0.2, etc
    for i in range(0, number):
        s = str(random.random())
        total += s[2]
    numberOfClass = 55
    tests = [False] * 10
    passed = 0
    tot = 0
    Kr = 0.0
    for alpha in alphas:
        #print("Test du Gap pour les décimales de Pi avec alpha = {0}".format(alpha))
        for i in range(0, len(tests)):
            tot += 1
            print("Pour la décimale {0} on a donc que:".format(i))
            test = gapTest(total, i, numberOfClass, alpha)
            Kr += test[1]
            if test[0]:
                passed += 1
                print("Le test du gap est donc réussi")
            else:
                print("Le test du gap à donc échouer")
    print("Le nombre de test réussi est de {0} sur {1} soit un pourcentage de {2}".format(passed, tot,((passed) / tot) * 100))
    return (((passed) / tot) * 100, Kr / tot)

def gapPi():
    """
    Test du gap sur les décimal de pi
    """
    pi = PiDecimalCounter.getPiDecimalNumber()
    numberOfClass = 55
    tests = [False] * 10
    for alpha in alphas:
        print("Test du Gap pour les décimales de Pi avec alpha = {0}".format(alpha))
        for i in range(0, len(tests)):
            print("Pour la décimale {0} on a donc que:".format(i))
            if gapTest(pi, i, numberOfClass, alpha)[0]:
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






