# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "C:\Python27\Programs\ProblemSet6\words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("C:\Python27\Programs\ProblemSet6\story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    alPH2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph = 'abcdefghijklmnopqrstuvwxyz'
    dict1 = {}
    dict2= {}
    check=0
    x=0
    for key in alPH2:
        if (shift + x) > 25 and check == 0:
            x=0
            check=1
            dict1[key] = alPH2[x]
            x+=1
        elif check==1:
            if shift>x:
                dict1[key] = alPH2[x]
                x+=1
            else:
                check==0
                break
        else:
            dict1[key] = alPH2[shift+x]
            x+=1
        
    check=0
    x=0
    for key in alph:
        if (shift + x) > 25 and check == 0:
            x=0
            check=1
            dict2[key] = alph[x]
            x+=1
        elif check==1:
            if shift>x:
                dict2[key] = alph[x]
                x+=1
            else:
                check==0
                break      
        else:
            dict2[key] = alph[shift+x]
            x+=1
    
    ndic = dict(dict1.items() + dict2.items())
    return ndic    
    
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    codedText = ''
    for letter in text:
        if letter in coder:
            codedText+=coder[letter]
        else:
            codedText+=letter
    return codedText
        
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    codedText = ''
    for letter in text:
        if letter in buildCoder(shift):
            codedText+=buildCoder(shift)[letter]
        else:
            codedText+=letter
    return codedText

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):         #Wordlist is a list of available words that has already been defined.
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    shift=0
    pos=0
    maxPos=0
    bestShift = 0
    while shift<26:
        splittedText = text.split(' ')            #Splits the text from a string to a list of words
        for word in splittedText:
            if isWord(wordList, word) == True:
                pos+=1
        if maxPos < pos:
            bestShift=shift
            maxPos=pos
            pos=0        
        shift+=1
        text = applyShift(text, 1)
   
    return bestShift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    return applyShift(getStoryString(), findBestShift(wordList, getStoryString()))    

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
  #  assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
