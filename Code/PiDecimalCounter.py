from Code import TestPi

'''
Compte le nombre de 0,1,2,3,... dans les décimale de Pi et les place dans une liste
Le i ème chiffre se trouve dans la i ème possition dans la liste retourner
'''
def countDigitFrequency():
    pi_f = open("../Files/pi.txt", "r")
    pi = ""
    for line in pi_f:
        pi += line.rstrip('\r \n')
    #On enleve le '3.14' de pi
    pi = pi[2:]
    count = [0,0,0,0,0,0,0,0,0,0]
    for number in pi:
        number = int(number)
        count[number] = count[number] + 1
    return count

if __name__ == '__main__':
    print(TestPi.chi2(countDigitFrequency()))
