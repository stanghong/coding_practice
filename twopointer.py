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

# 42. Trapping Rain Water
# difficulty is cannot think about this algo O(N) time and space

class Solution:
    def trap(self, height: List[int]) -> int:
        #algo min(l, r)-h[i]
        if len(height)==1: return 0

        maxleft=[0]*len(height)
        maxright=[0]*len(height)
        
        maxl=0

        for l in range(len(height)):
            maxl=max(maxl, height[l])
            maxleft[l]=maxl

        maxr=0
        for r in range(len(height)-1,-1, -1):
            maxr=max(maxr, height[r])
            maxright[r]=maxr
        
        vol=0
        for i in range(len(height)):
            vol+=min(maxleft[i], maxright[i])-height[i]
        
        return vol
