                    #Char in string with 'in' function

def isVowel2(char):
    '''
    char: a single letter of any case
    returns: True if char is a vowel and False otherwise.
    '''
    
    if char in 'aeiouAEIOU':
        x = True
    else:
        x = False

    return x
