       # two pointer approach O(LogN) time and O(N) space
        l, r = 0, len(numbers)-1
        while l < r:
            _sum =numbers[l]+ numbers[r] 
            if _sum == target:
                return [l+1, r+1]
            elif _sum > target:
                r -= 1
            else:
                l += 1
        
