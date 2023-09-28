# 8 string to integer
class Solution:
    def myAtoi(self, s: str) -> int:
        # clean string to only numbers and sign 
        #filter space
        #check sign
        #while is digit
 

        ans=0
        i=0
        sign=1
        val=0

        s=s.strip()
        if not s: return 0
        
        if i<len(s) and s[i]=='-':
            sign=-1
            i+=1
        elif s[i] == '+':
            i+=1

        while i<len(s):
            if s[i].isdigit():
                val=val*10+int(s[i])
            else:
                break
            i+=1

        val = sign * val
        val = max(val, -2**31)
        val = min(val, 2**31 - 1)

        return val
