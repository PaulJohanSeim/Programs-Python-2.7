# Copyright Paul-Johan Seim

# Recursive used for Hanoi Towers problems
def printMove(fr,to):
    print('move from' + str(fr)+'to' +str(to))
    
def Towers(n,fr,to,spare):
    if n==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1, fr, to, spare)
        Towers(n-1,spare,to,fr)
        
# Fibonacci: rabbits copulation increase-using multiple base cases
def fib(x):
    assert type(x)==int and x>=0 # Take an expression to check if it is true
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
