    #
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
print animals

print animals['d']                    #'donkey'
print len(animals)                    #4

animals['a'] = 'anteater'
print animals['a']                    #'anteater'
print len(animals['a'])                #8
print animals.has_key('baboon')        #Boolean-False
print 'donkey' in animals.values()    #Boolean-True
print animals.has_key('b')
print animals.keys()
del animals['b']
print animals
print len(animals)
print animals.values()