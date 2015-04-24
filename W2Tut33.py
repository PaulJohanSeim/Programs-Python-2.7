                                #Bisection search Assignment*
print('Please think of a number between 0 and 100!')

ans=0
numGuesses=0
low=0
y = ''
high=100
ans=(high+low)/2

while y != 'c':
    y = raw_input('Is your secret number ' +str(ans)+ '?\n'+ 'Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.')
    if y == 'h':
        high = ans
    if y == 'l':
        low = ans
    if y != 'c' and y != 'h' and y != 'l':
        print('Sorry, I did not understand your input.')
    ans=(high+low)/2


print('Game over. Your secret number was: ' +str(ans))
