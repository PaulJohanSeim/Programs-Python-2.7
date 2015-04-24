def McNuggets(n):
    a=0
    b=0
    c=0    
    n==6*a+9*b+20*c

    while c<=100:
        while b<=100:
            while a<=100:
                if n==6*a+9*b+20*c:
                    break
                a+=1
            if n==6*a+9*b+20*c:
                break
            a=0
            b+=1
        if n== 6*a+9*b+20*c:
            break
        b=0
        c+=1
    if n== 6*a+9*b+20*c:
        print a
        print b
        print c
        return True
    else:
        return False    