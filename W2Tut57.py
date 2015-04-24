        #Recursion-Palindrome     Divide and Conquer algorithm
def isPalindrome(s):

    def toChars(s):
        s = s.lower() #Internal function to convert s to lower case
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1]) #Last bit is slicing

    return isPal(toChars(s))
