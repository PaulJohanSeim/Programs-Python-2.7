    #Problem Set 3 - Third Issue
    #Printing out available items
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    resString=''
    alFa='abcdefghijklmnopqrstuvwxyz'
    for char in alFa:
        print char
        if char in lettersGuessed:
            resString=resString+''
        else:
            resString=resString+char
    
    return resString