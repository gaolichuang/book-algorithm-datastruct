'''
Candy
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''
class Solution(object):
  def candy(self, ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    if not ratings: return 0
    r = ratings
    lr = len(ratings)
    d = [1]*lr
    i = 1
    while i < lr:
      if r[i] > r[i-1]:
        d[i] = d[i-1]+1 if d[i] < d[i-1]+1 else d[i]
      i += 1
    sumc = d[lr-1]
    i = lr - 2
    while i >= 0:
      if r[i+1] < r[i]:
        d[i] = d[i+1]+1 if d[i] < d[i+1]+1 else d[i]
      sumc += d[i]
      i -= 1
    return sumc
s = Solution()
print s.candy([4,2,3,4,1])
#print s.candy([1,2,4,4,3])

