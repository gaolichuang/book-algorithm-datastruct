'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
'''
class FactorSeq(object):
  def __init__(self, factor):
    self.idx = 0
    self.factors = [1]
    self.factor = factor
  def nextfactor(self):
    v = self.fetch()
    self.idx += 1
    return v
  def addfactor(self, v):
    self.factors.append(v)
  def fetch(self):
    return self.factors[self.idx] * self.factor
class Solution(object):
  def nthUglyNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    f2 = FactorSeq(2)
    f3 = FactorSeq(3)
    f5 = FactorSeq(5)
    last,ugly = 1,1
    i = 0
    while i < n-1:
      u2 = f2.fetch()
      u3 = f3.fetch()
      u5 = f5.fetch()
      if u2 < u3:
        if u2 < u5:
          ugly = f2.nextfactor()
        else:
          ugly = f5.nextfactor()
      else:
        if u3 < u5:
          ugly = f3.nextfactor()
        else:
          ugly = f5.nextfactor()
      if ugly == last:
        continue
      f2.addfactor(ugly)
      f3.addfactor(ugly)
      f5.addfactor(ugly)
      last = ugly
      i += 1
      print ugly
    return ugly
s = Solution()
print s.nthUglyNumber(15)
