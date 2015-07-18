# Copyright Paul-Johan Seim

# Class Person

class Person (object):            #Class is the keyword, Person is the name of the object
    def __init__(self, name, age, height, weight):    #Parameters of an object called Person
        self.name = name                    #The underbars signify an magical method
        self.age = age
        self.height=height
        self.weight=weight
        
    def __str__(self):                #Underbar method
        return 'Name: ' +self.name+ ', Age: ' +str(self.age)+', Height: '+str(self.height)+', Weight: '+str(self.weight)

    def __eq__(self, other):          #Underbar method: Comparing method
        return self.name==other.name

mitch = Person('Mitch', 32, 70, 200)
sarina = Person('Sarina', 25, 65, 130)

print mitch
print sarina
print type(mitch)

print mitch==sarina            #Compare these two
