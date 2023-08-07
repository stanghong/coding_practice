# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # minheight and width max
        #left and right pointer
        res=0
        l,r=0, len(height)-1
        #shift left and right and update max area
        # shift shorter side till l r meets
        while l<r:
            area=(r-l)*min(height[l], height[r])
            res=max(res, area)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return res
