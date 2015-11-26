'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
    Given:
    s1 = "aabcc",
    s2 = "dbbca",

    When s3 = "aadbbcbcac", return true.
    When s3 = "aadbbbaccc", return false.

isInterleaving(s1,len1,s2,len2,s3,len3) 
        =   (s3.lastChar == s1.lastChar) && isInterleaving(s1,len1 - 1,s2,len2,s3,len3 - 1)
          ||(s3.lastChar == s2.lastChar) && isInterleaving(s1,len1,s2,len2 - 1,s3,len3 - 1)

'''
class Solution(object):
  def isInterleave(self, s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    s,t=s1,s2
    lens,lent = len(s),len(t)
    if not s1 and not s2 and not s3: return True
    if lens + lent != len(s3): return False
    d = [[-1]*(lens + 1) for k in range(lent+1)]
    for i in range(0,lens):
      if s[i] == s3[i]:
        d[0][i+1] = d[0][i] + 1
      else:
        break
    for i in range(0,lent):
      if t[i] == s3[i]:
        d[i+1][0] = d[i][0] + 1
      else:
        break
    for i in range(1,lent+1):
      for j in range(1,lens+1):
        print d[i-1][j]
        if d[i-1][j] >= 0 and t[i-1] == s3[d[i-1][j] + 1]:
          d[i][j] = d[i-1][j] + 1
        if d[i][j-1] >= 0 and s[j-1] == s3[d[i][j-1] + 1]:
          d[i][j] = d[i][j-1] + 1
    for i in d:
        print i
    return -1 != d[lent][lens]
s = Solution()
#s.isInterleave('aabcc','dbbca','aadbbcbcac')
#print s.isInterleave('aabcc','dbbca','aadbbbaccc')
#print s.isInterleave('aa','ab','abaa')
#print s.isInterleave('a','','a')
print s.isInterleave('a','b','ab')
