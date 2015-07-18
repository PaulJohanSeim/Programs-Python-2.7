# Copyright Paul-Johan Seim

# Recurring multiplication
def recurMul(a,b):
    if b==1:
        return a
    else:
        return a+recurMul(a,b-1)


# Factorial: Iterrative version
def fact(n):
    res=1
    while n>1:
        res*=n
        n-=1
    return res

# Shorter factorial: Recursive
def factR(n):
    if n == 1:
        return n
    return n*factR(n-1)
