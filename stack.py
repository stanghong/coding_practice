#853. Car Fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #monotinic decreasing stack
        # calculate time to end 
        #push to stack if increase popout till the end of list
        # time to finish
        fleet=[]
        pair=[(pos, spd) for pos, spd in zip(position, speed)]
        pair.sort(reverse=True) # ***order is very important, scan from right to left O(NlogN) time***
        for pos, spd in pair:
            tof=(target-pos)/spd
            fleet.append(tof) #create stack
            if len(fleet)>=2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        return len(fleet)

# 739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brutal force [73,74,75,71,69,72,76,73]; scan n! times O N^2 time 
                                # l   r
        #scan once monotonic decreasing stack
        if len(temperatures)==1: return [0]

        stack=[]
        for i, e in enumerate(temperatures):
            # stack.append(e)
            # while e> stack[-1]: pop and output[i]=i-stack[location] and i<len(nums)
            # else: stack. append((i,e)
            if not stack:
                stack.append((i, e))
            while stack and e > stack[-1][1]:
                temperatures[stack[-1][0]] = i-stack[-1][0] # if increase i-stack[-1[0]]
                stack.pop()
            else:
                stack.append((i, e))

            # following can be simplified as initialized res=[0]*len(temperature)
            if i==len(temperatures)-1: 
                while stack:
                    temperatures[stack[-1][0]]=0
                    stack.pop()

        return temperatures

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

#notice use minstack to save minval
# val <=selfminstack[-1] logic 
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
