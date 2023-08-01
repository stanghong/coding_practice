class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to lower case scan once
        _=[]
        for e in s:
            if e.isalnum():
                _.append(e.lower())
        # corner case
        if not len(_) or len(_) == 1 : 
            return True

        # compare left and right
        l,r=0,len(_)-1

        while l < r:
            if _[l] != _[r]:
                return False
            l+=1
            r-=1
        return True
        # O(N) time and space
