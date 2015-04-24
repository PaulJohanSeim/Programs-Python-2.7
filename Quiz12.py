def laceStrings(s1, s2):
    resultStr= ''
    n=0
    if len(s1)>len(s2):
        while len(s2)>n:
            resultStr+=s1[n]+s2[n]
            n+=1
        while len(s1)>n:
            resultStr+=s1[n]
            n+=1
        return resultStr
    else:
        while len(s1)>n:
            resultStr+=s1[n]+s2[n]
            n+=1
        while len(s2)>n:
            resultStr+=s2[n]
            n+=1
        return resultStr