import math
from scipy import stats

'''
Test du Chi2, Vrai si on accepte l'hypothèse, faux sinon
'''
def chi2(count):
    #La proba de chacun des intervale est de 10%, car il y a 10 intervale
    #probability_i = 0.1

    Kr = 0

    for i in range (0, len(count)):
        ni = count[i]
        Kr = Kr + (math.pow((ni - 100000), 2))/100000

    df = len(count) - 1
    alpha = 0.05
    critical = stats.chi2.ppf(1 - alpha, df)
    return critical >  Kr

