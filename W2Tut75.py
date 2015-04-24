import math
    #Radiation exposure - radioactivity decay
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    a=0.0
    t=0
    t=start
    z=0.0
    while t<stop:
        y=f(t)
        a=y*step
        print step
        print a
        z=sum((z,a))
        print z
        start+=1
        print t
        t+=step
    
    return z

def f(x):
    return 200*math.e**(math.log(0.5)/14.1*x)
    
    
    
    
    
    