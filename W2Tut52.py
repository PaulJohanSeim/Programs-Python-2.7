def recurMul(a,b):
    if b == 1:
        return a
    else:
        return a+recurMul(a, b-1)
        
def recurPower(base,exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base*recurPower(base, exp-1)