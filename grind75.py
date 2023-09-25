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

# 57. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #if inserted newInterval, just insert interval
        # if no overlap insert directly left
        # no overlap right, insert newInterval check if not inserted
        # if overlapped, updated newInterval left and right
      
        res=[]
        inserted=False
        for interval in intervals:

            if inserted: 
                 res.append(interval)
            elif interval[1] < newInterval[0]: #no overlap 
                res.append(interval)
            elif interval[0]>newInterval[1]: #no overlap 
                if not inserted: 
                    res.append(newInterval)
                    inserted=True
                res.append(interval)
            else: #hasOverlap
                newInterval[0]=min(interval[0],newInterval[0] )
                newInterval[1]=max(interval[1],newInterval[1] )
                # res.append(newInterval)

        if not inserted: # incase intervals is empty
            res.append(newInterval)      

        
        return res
