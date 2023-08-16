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
