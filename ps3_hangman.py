
def wordGuessed(secretWord, lettersGuessed):
    count=0
    for char in lettersGuessed:
        if char in secretWord:
            count+=1
    if char in secretWord:
        return True
    else:
        return False

def guessedWord(secretWord, lettersGuessed):
    resString=''
    for char in secretWord:
        if char in lettersGuessed:
            resString= resString + ' ' + char + ' '
        else:
            resString= resString + ' ' + '_' + ' '
    return resString

def availableLetters(lettersGuessed):
    alFa='abcdefghijklmnopqrstuvwxyz'
    resString=''
    for char in alFa:
        if char in lettersGuessed:
            resString=resString+''
        else:
            resString=resString+char
    return resString

def hangman(secretWord):
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' +str(len(secretWord))+ ' letters long.')
    print('------------')
    numGuesses=8
    print('You have '+str(numGuesses)+ ' guesses left')
    print('Available Letters: abcdefghijklmnopqrstuvwxyz')
        
    count=0
    z=''
    while True:
        z=z+str(raw_input("Please guess a letter: "))
        letterGuess = z.lower()
        guessString = guessedWord(secretWord, letterGuess)
        char = letterGuess[-1]
        n=0
        count3=0

        while n<1: 
            if letterGuess.count(char)>1:
                print("Oops! You've already guessed that letter: " +str(guessString))
                print('------------')
                print('You have ' +str(numGuesses)+ ' guesses left')
                print('Available Letters: ' +str(availableLetters(letterGuess)))
                break
            else:
                if wordGuessed(secretWord, letterGuess) == True:
                    count+=1
                    print('Good Guess: '+str(guessString))
                                   
                    for char in secretWord:
                        if char in letterGuess:
                            count3+=1
                    if count3 == len(secretWord):
                        break
                    print('------------')
                    print('You have ' +str(numGuesses)+ ' guesses left')
                    print('Available Letters: ' +str(availableLetters(letterGuess)))
                    break
                if wordGuessed(secretWord, letterGuess) == False:
                    print('Oops! That letter is not in my word: ' +str(guessString))
                    print('------------')
                    numGuesses-=1
                    if numGuesses==0:
                        break
                    print('You have ' +str(numGuesses)+ ' guesses left')
                    print('Available Letters: ' +str(availableLetters(letterGuess)))
            
            if wordGuessed(secretWord, letterGuess) == True and count==len(secretWord):
                break
            n+=1
        if count3 == len(secretWord):
            print('------------')
            print('Congratulations, you won!')
            break

        if wordGuessed(secretWord, letterGuess) == True and count==len(secretWord):
            print('------------')
            print('Congratulations, you won!')
            break  

        if numGuesses==0:
            print('Sorry, you ran out of guesses. The word was ' +str(secretWord)+'.')
            break
        
    return
