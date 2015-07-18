# Copyright Paul-Johan Seim

# Applying a list of functions to a variable x
def applyFuns(L, x):
    for f in L:
        print (f(x))

# applyFuns([abs, int], 4)

# Map function
S1=[1, -5, 20]
print map(abs, S1)
S2=[7, 2, 14]
print map(min, S1, S2)
