# 1. Two Sum
dic={}
for i, val in enumerate(nums):
    remain=target-val
    
    if remain in dic:
        return [dic[remain], i]
    else:
        dic[val] = i
#O(n) time

#36 valid suduku: learning defaultdict(set) no raise missing key error, tricks of i//3, i//3 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #data store in array board[i][j]
        #check repetition in row and columns
        # check repetition in 3x3 board[i][j] for _ in range(0, 9): for i etc.
        row= collections.defaultdict(set) #store all elements as collection of sets
        col= collections.defaultdict(set) #store all elements as collection of sets
        matrix= collections.defaultdict(set) #store all elements as collection of sets
        for i in range(0, 9): # check 3x3
            for j in range(0, 9): 
                if board[i][j] != '.':
                    if board[i][j] in matrix[(i//3, j//3)] \
                    or board[i][j] in row[i] \
                    or board[i][j] in col[j]:
                        return False
                    matrix[(i//3, j//3)].add(board[i][j])
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])

        return True

# 49. Group Anagrams
# O(N) Time and Space #learning of construction of keys
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create dictionary and key is the letters
        #use defaultdict(list)
        res=defaultdict(list)
        for e in strs:
            dic=[0]*26
            for s in e:
                loc = ord(s)-ord('a')
                dic[loc]+=1
            res[tuple(dic)].append(e)
        return res.values()
# method 2 simpler way to create key O(NKlog(K) Time
        res=defaultdict(list)
        for s in strs:
            key=sorted(s)
            res[tuple(key)].append(s)
        return res.values()

# 238. Product of Array Except Self
        #two lists, left2right and right2left and multiply together My solution
        # O(3N) time and O(3N)Space
        left2right=[1]*len(nums)
        for i in range(1, len(nums)):
            left2right[i]=left2right[i-1]*nums[i-1]

        right2left=[1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            right2left[i]=right2left[i+1]*nums[i+1]

        # find product
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=left2right[i]*right2left[i]

        return res

# 347. Top K Frequent Elements
    # method1 NlogN time compexity and log N space complexity
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create dictionary of counter, sort by counters
        #select highest freq elements

        countmap=dict(collections.Counter(nums))

        #sort by values
        sorteddict = dict(sorted(countmap.items(), key =lambda x: -x[1]) )
        print(sorteddict)
        #create list based on first k results
        res=[]
        i=0
        for key,v in sorteddict.items():
            if i<k:
                res.append(key)
            i+=1
        return res
    #method 2: dictionary using frequency as key
        
         #initialize the dictionary
        countdic=dict(collections.Counter(nums))
        dic=defaultdict(list)
       

        for key, freq in countdic.items():
            dic[freq].append(key)
        print(dic)
        
        res=[]
        for i in range(len(nums),-1, -1): # reverse freq so high not empty freq shows first
            if dic[i]: 
                res.extend(dic[i]) # use extend to handle nested list
        print(res)
        return res[:k]


