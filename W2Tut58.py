# Copyright Paul-Johan Seim

# Iterative version of counting the length of a string
def lenIter(aStr):
    count=0
    for letter in aStr:
        count+=1
    return count

# Recursive version of counting the length of a string
def lenRecur(aStr):
    while aStr!='':
         return 1 + lenRecur(aStr[1:])
    return 0

# Recursive version of Bisection of a character in string
def isIn(char, aStr):
    while True:
        if aStr=='':
            return False
        if char == aStr:
            return True
        if len(aStr) == 1 and char != aStr:
            return False
        if char == aStr[len(aStr)/2]:
            return True
        low=0
        high=len(aStr)
        x = (high+low)/2
        if char<aStr[x]:
            return isIn(char, aStr[0:x])
        elif char>aStr[x]:
            return isIn(char, aStr[x:len(aStr)])
        else:
            return False
        x= (high+low)/2
