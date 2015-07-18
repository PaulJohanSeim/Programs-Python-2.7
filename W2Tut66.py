# Copyright Paul-Johan Seim

# List functions
aList = range(1, 6)
bList = aList
aList[2] = 'hello'
aList == bList
print aList
cList = range(6, 1, -1)
dList = []
for num in cList:
    dList.append(num)
cList == dList
print cList
print dList
listA = [1, 4, 3, 0]
print listA
listA.sort             #<--Is a function
print listA
listA.sort()             #<--Is a Nonetype error
print listA             #<--Prints listA
listA.insert(0, 100)             #<--Is a function adding [100,0] to listA
print listA
listA.remove(3)             #<--Removes the number 3 from the string
print listA
listA.append(7)             #<--Adds 7 to the listA
print listA
listB = ['x', 'z', 't', 'q']
print listA+listB             #<--Concatanates two lists
listB.sort()             #<--Organizes listB into alphabetical order
print listB
listB.pop()             #<--Deletes the last element in listB
print listB
print listB.count('a')             #<--Counts the number of the letter a
print listB
listA.extend([4, 1, 6, 3, 4])             #<--Adds a new list of elements to listA
print listA
print listA.count(4)             #<--Counts the number of elements 4
print listA.index(1)             #<--Finds at what position the element 1 is at
print listA
listA.pop(4)             #<--Deletes the element at position 4
print listA
listA.reverse()             #<--Reverses the list of elements
print listA
