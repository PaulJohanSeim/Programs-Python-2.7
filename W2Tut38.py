                    # Two environments - function in a function
def square(x):
    return x*x
def twoPower(x,n):
    while n>1:
        x=square(x)
        n=n/2
    return x
    
def fourthPower(x):
    '''
    x: int or float.
    '''
    y = square(square(x))
    return y