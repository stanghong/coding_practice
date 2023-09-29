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
#longestr parlindrom (easy)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # create hashmap
        # even number +1 odd number is the maxlen
        hashmap=defaultdict(int)
        for e in s:
            hashmap[e]+=1
        evenCount=0
        oddCount=0
        for v in hashmap.values():
            if v%2 == 0:
                evenCount+=v
            else: # 'ccccc' can only use 4 cs
                evenCount+=v-1
                oddCount=1
        
        maxlen=oddCount+evenCount
        return maxlen
