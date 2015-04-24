s= 'Halloen du kordan gor det'
NumVow = 0
NumCo = 0
for char in s:
    if char=='a' or char =='e' or char=='i' or char=='o' or char == 'u':
        NumVow+=1
    else:
        NumCo+=1
print('Number of vowels: ' +str(NumVow))