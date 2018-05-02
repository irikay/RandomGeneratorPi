import math
from scipy import stats
from Code import PiDecimalCounter



'''
Test du Chi2 sur les decimal de Pi
'''
def chi2Pi():
    countPi = PiDecimalCounter.countDigitFrequency()
    #Il y a 10 chiffre dans la proba de chaque chiffre est de 10%
    proba = [1./10 * 1000000] * 10
    number = len(PiDecimalCounter.getPiDecimalNumber())
    return chi2(countPi, proba)

'''
Test du Chi2, Vrai si on accepte l'hypothèse, faux sinon

proba est les probabilités qu'on a eu
probaExp sont les probabiulité attendue théoriquement
'''
def chi2(proba, probaExp, alpha = 0.05):
    Kr = 0

    for i in range (0, len(proba)):
        ni = proba[i]
        Kr = Kr + (math.pow((ni - probaExp[i]), 2))/probaExp[i]

    df = len(proba) - 1
    critical = stats.chi2.ppf(1 - alpha, df)
    return critical >  Kr

'''
Test du gap sur les décimal de pi
'''
def gapPi():
    pi = PiDecimalCounter.getPiDecimalNumber()
    numberOfClass = 60
    tests = [False] * 10
    for i in range(0, 10):
        tests[i] = gapTest(pi, i, numberOfClass, alpha = 0.05)
    return tests

'''
Test du gap, retourne vrai si on accepte l'hypothèse, faux sinon
sequence est la sequence de nombre a analyser
number est le nombre qu'on va marqué
numberOfClasses est la taille maximal des trous qu'on va considéré entre 2 nombres marqué
'''
def gapTest(sequence, number, numberOfClasses,alpha):
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
    return chi2(classes, probaTheorical)

'''
Nous donne la valeur théorique pour un trou d'une certaine taille
'''
def getTheoricalProbaGap(gap):
    return (1.0/10)* math.pow(9.0/10, gap)

def poker():
    r = 10
    k = 5
    sn = sterling_number(r, k)


def sterling_number(r, k):
    if (k == 1) or (k == r):
        return 1
    else:
        return sterling_number(r-1, k-1) + (r * sterling_number(r, k-1))





