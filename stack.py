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

# 155. Min Stack

class MinStack:


    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val<= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:

        if self.stack:
            if self.minstack[-1] == self.stack[-1]: #if pop the minimal
                self.minstack.pop()
            self.stack.pop()
        
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            print('the stack is empty')
        

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        else: 
            print('minstack is empty')
