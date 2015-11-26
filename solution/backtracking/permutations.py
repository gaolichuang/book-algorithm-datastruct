import copy

class Solution(object):
  '''
    但是注意这里不是所有x及其后面的数字都能够选择，因为可能这个数字已经选过了，
    再次选择会导致出现重复的结果，
    解决的办法是在每次选择之前先扫描一次看该数字是否在x之后自身位置之前是否已经出现过了，如果没有才可以进行选择。
  '''
  def dfs(self, num, idx, n, rets):
    if idx >= n:
      rets.append(copy.deepcopy(num))
      return
    pre = []
    for i in range(idx, n):
      if num[i] in pre: continue
      pre.append(num[i])
      num[idx],num[i] = num[i],num[idx]
      self.dfs(num, idx + 1, n, rets)
      num[idx],num[i] = num[i],num[idx]

  def permute2(self, num):
    rets = []
    self.dfs(sorted(num), 0, len(num), rets)
    return rets

  def permuteUnique(self, num):
    length = len(num)
    if length == 0: return []
    if length == 1: return [num]
    num.sort()
    res = []
    previousNum = None
    for i in range(length):
      if num[i] == previousNum: continue
      previousNum = num[i]
      for j in self.permuteUnique(num[:i] + num[i+1:]):
        res.append([num[i]] + j)
    return res
  def permute(self, num):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(num) == 0: return []
    if len(num) == 1: return [num]
    res = []
    for i in range(len(num)):
      for j in self.permute(num[:i] + num[i+1:]):
        res.append([num[i]] + j)
    return res
s = Solution()
print s.permute2([1,2,3,4])
print s.permuteUnique([1,2,3,4])
print s.permute2([0,0,0,1,9])
print s.permuteUnique([0,0,0,1,9])
#print s.permute([1,2,3])

