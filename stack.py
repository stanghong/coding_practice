# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        # sue deque for stack
        dic={')':'(', ']':'[', '}':'{' }

        dq=deque()

        if s[0] in dic or len(s)==1: # corner case
            return False
        "(){}}{"
        for i, e in enumerate(s):
            # print(dq)
            if e not in dic:
                dq.appendleft(e)
            elif dq and dic[e] == dq[0]: # note check dq before check match
                dq.popleft()
            else:
                dq.appendleft(e)
        
        if dq:
            return False
        else:
            return True
