                        # Two different functions separately

def square(x):
    z=x**2
    return z

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    z= a*x**2 + b*x + c
    return z