from Code import TestPi

'''
Compte le nombre de 0,1,2,3,... dans les décimale de Pi et les place dans une liste
Le nombre d'occurence du i ème chiffre se trouve dans la i ème position dans la liste retourner
'''
def countDigitFrequency():
    pi = getPiDecimalNumber()
    count = [0,0,0,0,0,0,0,0,0,0]
    for number in pi:
        number = int(number)
        count[number] = count[number] + 1
    return count

'''
Retourne toutes les decimales de pi
'''
def getPiDecimalNumber():
    pi_f = open("../Files/pi.txt", "r")
    pi = ""
    for line in pi_f:
        pi += line.rstrip('\r \n')
    # On enleve le '3.14' de pi
    return pi[2:]

if __name__ == '__main__':
    #Test Chi2 sur les decimal de Pi, alpha = 0.05
    print(TestPi.chi2Pi())

    #Test du gap sur les decimal de Pi, alpha = 0.05
    testGap = TestPi.gapPi()
    for i in range(0, len(testGap)):
        print(testGap[i])
