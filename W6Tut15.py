def genTest():
    yield 1
    yield 2

print genTest()

def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        #fib(n)=fib(n-1) + fib(n-2)
        next =fibn_1 + fibn_2
        yield next
        fibn_2=fibn_1
        fibn_1=next
    
fib=genFib()
print fib.next()
print fib.next()

def genPrimes():
    x=1
    primes = []
    while True:
        x+=1
        for p in primes:
            if x % p == 0:
                break
        else:
            primes.append(x)
            yield x

                    
