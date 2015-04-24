                    #Two same boolean functions with either if condition or while condition

def isVowel(char):
    '''
    char: a single letter of any case
    returns: True if char is a vowel and False otherwise.
    '''
    True = char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'
    y = False
    while char:
        y = True
        break
    return y
print isVowel('g')

def isVowel(char):
    '''
    char: a single letter of any case
    returns: True if char is a vowel and False otherwise.
    '''
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        y = True
    else:
        y = False
   
    return y
