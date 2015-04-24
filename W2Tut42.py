                    #Boolean comparaison without if statement
def odd(x):
    '''
    x: int or float.
    returns: True if x is odd, False otherwise
    '''
    y = False
    while x%2 == 1:
        y = True
        break
        
    return y
