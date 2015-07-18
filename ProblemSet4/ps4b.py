# Copyright Paul-Johan Seim


from ps4a import *
import time


def isValidWord(word, hand, wordList):
    count=0
    feil=0
    for char in word:
        t=word.count(char)
        if char in hand and t<= hand.get(char,0):
            count+=t  
        else:
            feil+=1    
    if feil==0 and len(word)<=count:
        return True
    else:
        return False

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

def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line

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



#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    maxScore=0
    score=0
    bestWord=''
    word =''

    
    for word in wordList:
        if isValidWord(word, hand, wordList) == True:
            score=getWordScore(word, n)
            if score>maxScore:
                maxScore=score
                bestWord = word
            #print bestWord
            #print maxScore
    if score>0:
        return bestWord
    else:
        return None
        

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):


    totalScore=0
    score=0
    
    
    while True:
        tomt=0
        print
        print "Current Hand:", 
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
                
        
        if word == None:
            break
        else:
            print
            totalScore+=getWordScore(word, n)
            print ("'"),
            print word,
            print "'",
            print('earned ' +str(getWordScore(word, n)) + ' points. Total: '+ str(totalScore) + ' points')
            hand = updateHand(hand, word)
            for char in hand:
                
                tomt+= hand.get(char, 0)
                
        print tomt
        if tomt == 0:
            break
    print
    if word== None:
        print('her')
        print('Total score: ' +str(totalScore)+ ' points.')
        return
    print('Total score: ' +str(totalScore)+ ' points.')
    return
    
    
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):

    n = HAND_SIZE
    tag=0
    hand={}
    s=0
    while True:
        while True:
            decision = str(raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
            if decision == 'e'or decision == 'n':
                break
            elif decision == 'r':
                print hand
                if s==0:
                    print('You have not played a hand yet. Please play a new hand first!')
                else:
                    break
            else:
                print('Invalid command.')
                print
                
        if decision == 'e':
            break      
        while True:
            decision2 = str(raw_input('Enter u to have yourself play, c to have the computer play: '))
            if decision2 == 'u' or decision2 == 'c':
                break
            else:
                print('Invalid command.')
                print                
               
        if decision == 'n':
            hand = dealHand(n)
            tag=1
        elif decision == 'r':
            if tag == 0:
                print('You have not played a hand yet. Please play a new hand first!')
            
        if decision2 == 'u':
            playHand(hand, wordList, n)
        if decision2 == 'c':
            compPlayHand(hand, wordList, n)
        s=1
    return



        

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


