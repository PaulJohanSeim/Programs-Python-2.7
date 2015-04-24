def recurPowerNew(base, exp):
    if exp==0:
        return 1
    if exp>0 and exp %2==0: #even
        return recurPowerNew(base*base,exp/2)
    if exp>0 and exp%2==1: # odd
        return base*recurPowerNew(base,exp-1)

def gcdIter(a, b): #Returns the biggest common denominator between two positive numbers
    testVal = min(a,b)
    testVal2= max(a,b)
    rest=testVal2%testVal
    c=testVal
    while c>0:
        if testVal2%c ==0 and testVal%c == 0:
            print c
            return c
        print c
        c-=1
    return rest

def gcdRecur(a, b): #Recursive method of finding the biggest common denominator with Euclid's law
    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)



