'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
Ensure that numbers within the set are sorted in ascending order.
Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution(object):
  def combinationSum3(self, k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    rets = []
    self.dfs(range(1,n+1), n, k, [], rets)
    return rets

  def dfs(self, can, n, k, ans, rets):
    '''
      ans is index at can
    '''
    if len(ans) > k:
      return
    if len(ans) == k and n == 0:
      import copy
      rets.append(copy.deepcopy(ans))
      return
    start = ans[-1] + 1 if ans else 1
    for i in range(start, len(can)):
      ans.append(i)
      self.dfs(can, n - i,k, ans, rets)
      ans.pop()
s = Solution()
print s.combinationSum3(3,9)
