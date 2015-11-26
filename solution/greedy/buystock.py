'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    p = prices
    lens = len(prices)
    if lens < 2:
      return 0
    profit = 0
    idx = 1
    while idx < lens:
      while idx < lens and p[idx] <= p[idx - 1]: idx += 1
      if idx >= lens: return profit
      mint = p[idx-1]
      while idx < lens and p[idx] >= p[idx - 1]: idx += 1
      maxt = p[idx-1]
      profit += maxt - mint
      if idx >= lens: return profit
    return profit
s = Solution()
print s.maxProfit([1,2])
print s.maxProfit([2,1])
print s.maxProfit([1,2,1,2,1])
print s.maxProfit([2,1,2,1])
