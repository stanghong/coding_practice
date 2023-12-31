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

# 340. Longest Substring with At Most K Distinct Characters
  l, r = 0, 0
    maxlen = 0
    char_count = defaultdict(int)
    
    while r < len(s):
        char_count[s[r]] += 1
        
        while len(char_count) > k: 
            char_count[s[l]] -= 1
            if char_count[s[l]] == 0:
                del char_count[s[l]]
            l += 1
        
        maxlen = max(maxlen, r - l + 1)
        r += 1
        
    return maxlen

#159  Longest Substring with At Most Two Distinct Characters
def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #sliding window, 
        l, r =0, 0
        map=defaultdict(int)
        maxlen=0
        for r in range(len(s)):
            map[s[r]]+=1
            while len(map)>2:
                map[s[l]]-=1
                if map[s[l]]==0:
                    del map[s[l]]
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen


# Grokking: a list of starting indices of the anagrams of the pattern in the given string.
from collections import defaultdict
def find_string_anagrams(str1, pattern):
  result_indexes = []
  # TODO: Write your code here
  l, r =0, 0
  pat=defaultdict(int)
  map=defaultdict(int)
  # initialize pattern dict
  for e in pattern:
     pat[e]+=1
  print(str1, pattern)
  #sliding window
  for r in range(len(str1)):
    map[str1[r]]+=1
    while len(map)>=len(pat): 
      print(pat, map)
      if pat == map:
          result_indexes.append(l) 
      map[str1[l]]-=1
      if map[str1[l]] == 0:
        del map[str1[l]]
      l+=1

      
  return result_indexes
