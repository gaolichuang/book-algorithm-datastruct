'''
Perfect Squares My Submissions Question
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
    which sum to n.
For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

if X = a + b*b
 f(X) = f(a) + 1
'''
class Solution(object):
  def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    import sys
    ret = [sys.maxint]*(n+1)
    i = 1
    while i*i <= n:
      ret[i*i] = 1
      i += 1
    i = 0
    while i <= n:
      b = 1
      while i + b*b <= n:
        if ret[i] + 1 < ret[i+b*b]:
          ret[i+b*b] = ret[i] + 1
        b += 1
      i += 1
    print ret
    return ret[n]
s = Solution()
print s.numSquares(12)
print s.numSquares(5238)

