        #What is the sum of the values in a dictionary
def howMany(aDict):
    count=0
    for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ':
        if aDict.has_key(char)==False:
            ()
        else:
            count+=len(aDict[char])
    return count

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print animals['d']
print len(animals['d'])
