# Copyright Paul-Johan Seim
                    
# Function of max of three numbers

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    a=lo
    b=x
    c=hi
    a<c
    
    y = min(max(a, b), c)
    
    return y
       

        
        

