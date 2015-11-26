'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''
'''
if s[i] == t[j]:
d[i][j] = d[i-1][j-1] + d[i-1][j] # not del or  del
else
d[i][j]=d[i-1][j] # del
'''
class Solution(object):
  def numDistinct(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    lens,lent = len(s),len(t)
    d = [[0]*(lens + 1) for k in range(lent+1)]
    d[0][0] = 1
    for i in range(lens):
      d[0][i] = 1
    for i in range(lent):
      for j in range(lens):
        if t[i] == s[j]:
          if d[i][j] >=1:
            d[i+1][j+1] = d[i][j] + d[i+1][j]
          elif d[i+1][j] > 0:
            d[i+1][j+1] = 1 + d[i+1][j]
          else:
            d[i+1][j+1] = d[i+1][j]
        else:
          d[i+1][j+1] = d[i+1][j]
    for i in d:
        print i
    return d[lent][lens]
s = Solution()
print s.numDistinct('rabbbit','rabit')
print s.numDistinct('aaa','aa')
print s.numDistinct('aacaacca','ca')

