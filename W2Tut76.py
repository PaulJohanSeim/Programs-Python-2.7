# Copyright Paul-Johan Seim

# First Issue
def isWordGuessed(secretWord, lettersGuessed):
    count=0
    for char in lettersGuessed:
        print char
        if char in secretWord:
            print char
            count+=1
           
    print count
    print len(secretWord)
    if count == len(secretWord):
        return True
    else:
        return False
