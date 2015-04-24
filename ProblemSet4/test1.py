WORDLIST_FILENAME = "C:/Python27/Programs/ProblemSet4/words.txt"
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
import random
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
       

def isValidWord(word, hand, wordList):
    count=0
    if word in wordList:
        for char in hand:
            n=word.count(char)
            if n<= hand.get(char,0):
                count+=n
            else:
                ()
    else:
        return False
    if len(word)==count:
        return True
    else:
        return False

def updateHand(hand, word):
    handUpdated={}
    for char in hand:
        n=word.count(char)
        if word.count(char)>1 and char in word:
            handUpdated[char]=hand.get(char,0)-n
        elif char in word:
            handUpdated[char]= hand.get(char,0)-1
        else:
            handUpdated[char]= hand.get(char,0)
    return handUpdated

def getWordScore(word, n):
    count=0
    for char in word:
        if char in SCRABBLE_LETTER_VALUES:
            count+=SCRABBLE_LETTER_VALUES[char]
        else:
            ()
    count*=len(word)
    if len(word)==n:
            count+=50
    return count


def dealHand(n):
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    print hand
    return hand

def playHand(hand, wordList, n):

    totalScore=0
    score=0
    while True:
        ferdig=0
        print
        print "Current Hand: ", 
        displayHand(hand)
        word = str(raw_input('Enter word, or a "." to indicate that you are finished: '))

        if word == '.' or word == '':
            break     
        if isValidWord(word, hand, wordList)!=True:
            print "Invalid word, please try again."
        else:
            score = getWordScore(word, n)
            totalScore+=score
            print(str(word) + ' earned ' +str(getWordScore(word, n)) + ' points. Total: '+ str(totalScore) + ' points')
            hand = updateHand(hand, word)
            for char in hand:
                if hand[char]==0:
                    ferdig +=1
            if ferdig==len(hand):
                break
    
    if word == '.' or word == '':
        print
        print('Goodbye! Total score: ' +str(totalScore)+ ' points.')
        ferdig=1
        return 
    if ferdig==len(hand):
        print
        print('Run out of letters. Total score: ' +str(totalScore)+ ' points.')
        return 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    n = HAND_SIZE
    tag=0
    
    while True:
        decision = str(raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if decision == 'n':
            hand = dealHand(n)
            tag=1
            playHand(hand, wordList, n)
        elif decision == 'r':
            if tag == 0:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(hand, wordList, n)
        elif decision == 'e':
            break
        else:
            print('Invalid command.')
            
    return
    







