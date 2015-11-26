'''
Palindrome Partitioning II
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
class Solution(object):
  def ispal(self, s, start, end):
    i,j = start,end
    while i < j:
      if s[i] != s[j]:
        return False
      i,j = i+1,j-1
    return True

  def minCut(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s: return 0
    ls = len(s)
    p = [-1]*(ls+1)
    for i in range(1,ls+1):
      mins = ls
      for j in range(0,i):
        if s[i-1] != s[j]: continue
        if self.ispal(s,j,i-1):
          mins = p[j]+1 if mins > p[j]+1 else mins
      p[i] = mins
    print p
    return p[ls]

s = Solution()
print s.minCut('aabcdef')
