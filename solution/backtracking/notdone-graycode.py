'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

'''
class Solution(object):
  def grayCode(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    rets = []
    self.dfs([0]*n,0,'',rets)
    return rets

  def dfs(self,n,idx,ans,rets):
    if idx == len(n):
      print ans
      return

      self.dfs(n,idx+1,ans + i,rets)

s = Solution()
s.grayCode(3)

