s='abchjel'
i=0

while((i<(len(s)-1))and(s[i]<=s[i+1])):
    i += 1
    if i==(len(s)-1):
        break
        
print i