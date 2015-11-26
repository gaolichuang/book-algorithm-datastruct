'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
    Return

      [
      ["aa","b"],
      ["a","a","b"]
      ]
'''
class Solution(object):
  def partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    rets = []
    self.p(s,[],rets)
    return rets
  def p(self, s, ret, rets):
    import copy
    if len(s) == 0:
      rets.append(copy.deepcopy(ret))
      print ret
      return
    for i in range(1, len(s)+1):
      if not self.isp(s[:i]):
        continue
      ret.append(s[:i])
      self.p(s[i:],ret,rets)
      ret.pop()
  def isp(self, s):
    i,j = 0,len(s)-1
    while i<j:
      if s[i] != s[j]:
        return False
      i = i+1
      j = j-1
    return True
s = Solution()
#s.partition('abcdef')
#print s.partition('aab')
print s.partition('a')
