                # Two environments with global and local assignments


def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print('iteration: ' +str(turn) + 'current result: ' + str(result))
        result = result*x
    return result
    
print result