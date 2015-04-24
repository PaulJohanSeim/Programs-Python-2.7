def laceStringsRecur(s1, s2):
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[0]+s2[0] + helpLaceStrings(s1[1:], s2[1:], out)
    return helpLaceStrings(s1, s2, '')