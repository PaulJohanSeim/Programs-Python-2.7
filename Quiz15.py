def fixedPoint(f, epsilon):
    print f
    guess = 1.0
    for i in range(100):
        if f(guess) - 1.4 < epsilon:
            return guess
        else:
            guess = f(guess)-1
            print guess
    return guess

def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit(a), 0.0001)