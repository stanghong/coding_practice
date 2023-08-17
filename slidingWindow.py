# sliding window
# 121 max price ...sliding window green
  l ,r = 0, 0
  maxprofit = 0
  while r < len(prices):
      maxprofit = max(maxprofit, prices[r] -prices[l] )
      print(l, r, maxprofit)
      if prices[l]>prices[r]:
          l = r
      r += 1
  return maxprofit
  # O(N) time and O(1) Space

# 424. Longest Repeating Character Replacement yellow-redo
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        l, r =0, 0
        maxlen, maxFreq = 0, 0
        map ={}
        while r < len(s):
            map[s[r]] = map.get(s[r], 0) + 1
            maxFreq =max(maxFreq, map[s[r]])

            if (r-l+1 - maxFreq) > k: # # stop condition
                map[s[l]] -= 1
                if not map[s[l]]: 
                    map.pop(s[l])
                l += 1
            else:           
                maxlen= max(maxlen, r-l+1)
            r += 1
        return maxlen
