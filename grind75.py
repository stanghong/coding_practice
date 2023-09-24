# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by 1
        #compare the second if left[1]>right[0] and left[1]=maxleft[1], right[2]) and append(new interval)
        res=[]
        intervals.sort(key=lambda x: x[0] )

        for interval in intervals:
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1]=max(res[-1][1], interval[0], interval[1])

        return res
