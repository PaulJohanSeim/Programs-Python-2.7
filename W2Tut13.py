# Copyright Paul-Johan Seim

s = 'bobobobobobobobob'

count= 0
result=0
for char in s:
    if s[count:count+3]=='bob':
        result+=1
    else:
        ()

    count += 1
print('Number of times bob occurs is: '+str(result))

