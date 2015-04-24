    #Divide each element in a list by 4
                #From testList = [1, -4, 8, -9]
def timesFive(a):    #Aims is [5, -20, 40, -45]
    return a*5
def absolute(a):      #Aim is [1, 4, 8, 9]
    return abs(a)
def addition(a):      #Aim is [2, -3, 9, -8]
    return 1+a
def power(a):         #Aim is [1, 16, 64, 81]
    return a**2

def applyToEach(L, power):
    #L = [1, -4, 8, -9]
    for i in range(len(L)):
        L[i] = power(L[i])
    return L