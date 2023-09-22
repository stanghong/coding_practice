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

# three sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #three sum is two sum +two sum
        # sorted, two pointers
        # -1,0,1,2,-1,+4 1,2,3, 5
        # N2 time
        ans=[]
        nums.sort()
            
        for i, e in enumerate(nums):
            if e >0: break

            if i> 0 and nums[i] ==nums[i-1]: # duplicates
                continue

            l,r=i+1, len(nums)-1
            while l < r:
                _sum=nums[l]+nums[r]+e
                if _sum < 0:
                    l+=1
                elif _sum>0:
                    r-=1
                else:
                    ans.append([nums[l], nums[r],e]) #find one answer
                    l+=1    #keep moving on
                    r-=1
                    while nums[l]==nums[l-1] and l<r: #treat duplicates
                        l+=1

# remove duplicates from a list Grokking pattern
def remove_duplicates(arr):
  # TODO: Write your code here
  # two pointer
  # [2, 3, 3, 3, 6, 9, 9]
  #              l
  #                    r
  l, r =0, 1
  while r <len(arr):
    if arr[r] != arr[l]:
      l+=1
      arr[l] =arr[r]
    r+=1
return l+1

#triplet_sum_close_to_target
def triplet_sum_close_to_target(arr, target_sum):
  arr.sort()
  closetSum =float('inf') # note inf usage
  small_diff=float('inf')
  for i in range(len(arr)-2): #note i
    l, r = i+1, len(arr) -1
    while l < r:
      _sum=arr[l]+arr[r]+arr[i]
      diff=abs(_sum-target_sum)
      if diff<small_diff:
        small_diff=min(diff, closeSum)
        closetSum=_sum

      if _sum < target_sum:
        l+=1
      else:
        r-=1

  return closetSum
