import copy
class Solution(object):
  '''
  Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
  '''
  def combine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    rets = []
    self.dfs(range(1, n + 1), 0, k, [], rets)
    return rets
  def dfs(self, n, idx, k, ret, rets):
    if idx == k:
      rets.append(copy.deepcopy(ret))
      print ret
      return
    start = ret[-1] if ret else 1
    for i in range(start, len(n) + 1):
      if i in ret:
        continue
      ret.append(i)
      self.dfs(n, idx + 1, k, ret, rets)
      ret.pop()
s = Solution()
print s.combine(4,2)
#print s.combine(5,2)
