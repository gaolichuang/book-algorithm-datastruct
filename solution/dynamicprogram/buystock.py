'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

'''
class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
      return 0
    maxp = prices[1] - prices[0]
    maxp = 0 if maxp < 0 else maxp
    minp = prices[0] if prices[0] < prices[1] else prices[1]
    for n in prices[2:]:
      if n < minp:
        minp = n
      if n - minp > maxp:
        maxp = n - minp
      print minp,maxp
    return maxp
s = Solution()
print s.maxProfit([2,1])
print s.maxProfit([1,2])
#print s.maxProfit([1,2,3,4,5,6])
