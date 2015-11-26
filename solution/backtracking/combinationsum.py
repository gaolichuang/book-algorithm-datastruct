'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2,... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
    A solution set is: 
    [7] 
    [2, 2, 3] 
'''
class Solution(object):
  def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    rets = []
    self.dfs(candidates, target, [], rets)
    return rets
  def dfs(self, can, target,ans,rets):
    if target == 0:
      import copy
      rets.append(copy.deepcopy(ans))
      return
    for c in can:
      if c > target:
        continue
      if ans and c < ans[-1]:
        continue
      ans.append(c)
      self.dfs(can, target - c, ans, rets)
      ans.pop()
s = Solution()
print s.combinationSum([2,3,6,7],7)
