class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        # search on row first and binary on the row
        #scan rows
        if matrix[0][0]>target or matrix[-1][-1]<target:
            return False

        for lst in matrix:
            l, r =0, len(lst)-1
            if lst[0] <= target  and lst[-1] >= target:
                
                while l <= r:
                    m = (l+r)//2
                    if lst[m] == target:
                        return True
                    elif lst[m] < target :
                        l = m + 1
                    else:
                        r = m - 1
        
        return False

# 875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #count pile[i]//k = hr hr<=8 for mini hr
        # k=[1, sum[bananas] if eat one] bananas can scan 
        # find the target sum(hr)<= h--> binary search

        totBan=max(piles)
        l, r =1, totBan
        res=max(piles)

        while l <= r:
            m= (l+r)//2
           
            hrEat = 0
            for e in piles:
                hrEat+=math.ceil(e/m)

            # learned the stop criteria res = min(res, m) for selecting min, max
            # move from left so the res decreasing find minimum; from to right find max

            if hrEat <= h: # too slow
                res = min(res, m)
                r = m - 1
            else: # too fast
                l = m + 1

        return res

# 153. Find Minimum in Rotated Sorted Array
        # note nums[l] < nums[m] doesn't work  explaination below.
        # otherwise, other conditions work

        l, r = 0, len(nums)-1

        if len(nums) == 1: return nums[0]
        res= float(inf)

        while l < r:
            m = (l+r)//2
            res = min(res, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m -1
        return min(res, nums[l])

# Let's walk through the scenario of [4,5,6,7,0,1,2] to see why nums[l] < nums[m] doesn't work as expected:

# Initially, l = 0 and r = 6.
# The middle element is m = 3, which is 7. The condition nums[l] < nums[m] holds (4 < 7), so we update l = m + 1 to l = 4.
# Now, l = 4 and r = 6.
# The middle element is m = 5, which is 1. Here, the condition nums[l] < nums[m] doesn't hold (4 is not less than 1), so we update r = m to r = 5.
# At this point, both l and r point to index 5, and you've effectively skipped the pivot element 0. This is why the condition nums[l] < nums[m] fails to handle the pivot element correctly and doesn't provide the desired result.

# 33. Search in Rotated Sorted Array
# steps, look left or right and search left or right; 
# and hangle corner case [1]
        l, r = 0, len(nums) -1


        while l <= r:
            m = (l+r)//2

            if nums[m] == target: return m # find it

            if nums[l] <= nums[m]: # =? left sorted
                if (target < nums[l] or target > nums[m]) : #look left or right
                    l = m + 1
                else:
                    r = m - 1
            else: #right sorted 
                if (target < nums[m] or target > nums[r]) : #look left or right
                    r = m -1
                else:
                    l = m+ 1

        return -1
            

