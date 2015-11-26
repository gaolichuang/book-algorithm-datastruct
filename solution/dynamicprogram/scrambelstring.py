'''
Scramble String My Submissions Question

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of s1 = "great":

      great
      /    \
    gr    eat
    / \    /  \
   g   r  e   at
             / \
            a   t
To scramble the string, we may choose any non-leaf node and swap its two children.
For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
        rgeat
        /    \
       rg    eat
      / \    /  \
     r   g  e   at
               / \
              a   t
We say that "rgeat" is a scrambled string of "great".
Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

      rgtae
      /    \
    rg    tae
    / \    /  \
   r   g  ta  e
          / \
         t   a
We say that "rgtae" is a scrambled string of "great".
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''
class Solution(object):
  def isScramble(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    return self.dfs(s1,s2)
  def dfs(self,s1,s2):
    if len(s1) != len(s2): return False
    if len(s1) == 1 and s1 != s2:   return False
    if s1 == s2: return True
    for i in range(len(s1)):
      ret = self.dfs(s1[:i], s2[:i]) and self.dfs(s1[i+1:], s2[i+1:])
      ss2 = ''.join(reversed(list(s2)))
      ret = ret or (self.dfs(s1[:i], ss2[:i+1]) and self.dfs(s1[:i], ss2[:i+1]))
      if ret == True:
        return True
    return False
s = Solution()
print s.isScramble('great','rgtae')
print s.isScramble('great','retag')
print s.isScramble('c','b')
