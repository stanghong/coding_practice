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
                        l += 1
                    else:
                        r -= 1
        
        return False
