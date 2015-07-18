# Copyright Paul-Johan Seim

# Find biggest key in a dictionary, i.e. the key that contains the most values

def biggest(aDict):
    count=0
    var=0
    for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ':
        if aDict=={}:
            return None
        if aDict=={char:[]}:
            return char        
        if aDict.has_key(char)==False:
            ()
        else:
            if len(aDict[char])>count:
                count=len(aDict[char])
                var = char
    return var

#aDict = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd':['djangoo'],
#'e':['epler'], 'f':['felle'], 'g':['gangsperre', 'geilo', 'gelender'], 'h':['holdbarhetsdato'], 'i':['inntekt'], 
#'j':['julenisse']}     'g' is the answer
    
    
    
