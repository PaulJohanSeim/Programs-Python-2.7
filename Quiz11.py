def myLog(x, b):
    n=0
    while (b**n)<=x:
        n+=1
        print n
        print b**n
    return n-1