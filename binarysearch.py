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

