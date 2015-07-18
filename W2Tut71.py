# Copyright Paul-Johan Seim

monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 1:'Jan', 2:'Feb', 3:'Mar'}
print monthNumbers
print monthNumbers['Feb']
print monthNumbers[3] #No index possible, i.e. [0]
monthNumbers['Apr']=4
print monthNumbers['Apr']

    #Iteration
collect=[]
for e in monthNumbers:
    collect.append(e)
print collect
print monthNumbers.keys() #Method

    #Tuple-immutable, hence good for libraries
myDict = {(1,2):'twelve', (1,3):'thirteen'}
print myDict[(1,2)]
