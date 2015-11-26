'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2,... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
    A solution set is: 
    [1, 7] 
    [1, 2, 5] 
    [2, 6] 
    [1, 1, 6] 
'''
class Solution(object):
  def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    rets = []
    self.dfs(sorted(candidates), target, [], rets)
    return rets

  def dfs(self, can, target, ans, rets):
    '''
      ans is index at can
    '''
    if target <= 0:
      print ans
      rets.append([can[k] for k in ans])
      return
    last = None
# make sure index is incress, no dumplicate
    start = ans[-1] + 1 if ans else 0
    for i in range(start, len(can)):
      c = can[i]
      if last == c:
        continue
      if c > target:
        continue
      last = c
      ans.append(i)
      self.dfs(can, target - c, ans, rets)
      ans.pop()
s = Solution()
#print s.combinationSum2([10,1,2,7,6,1,5],8)
#print s.combinationSum2([1,2],4)
#print s.combinationSum2([1],1)
#print s.combinationSum2([4,4,2,1,4,2,2,1,3],6)
print s.combinationSum2([1,1,1,2,2,2,4],6)
