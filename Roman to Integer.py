class Solution(object):
    def romanToInt(self, s):
        symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        
        l = len(s)
        # print(l)
        #Storing  the result
        result = symbols[s[l - 1]]
        # print(result)
        #Checking with a for loop
        for i in range(l - 2, -1, -1):
            if symbols[s[i]] >= symbols[s[i+1]]:
                result += symbols[s[i]]
            else:
                result -= symbols[s[i]]
                
        return result
        
        