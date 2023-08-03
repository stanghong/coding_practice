# 1. Two Sum
dic={}
for i, val in enumerate(nums):
    remain=target-val
    
    if remain in dic:
        return [dic[remain], i]
    else:
        dic[val] = i
#O(n) time
