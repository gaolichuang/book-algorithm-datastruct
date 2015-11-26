'''
Wildcard Matching My Submissions Question

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

    Some examples:
    isMatch("aa","a")  false
    isMatch("aa","aa")  true
    isMatch("aaa","aa")  false
    isMatch("aa", "*")  true
    isMatch("aa", "a*")  true
    isMatch("ab", "?*")  true
    isMatch("aab", "c*a*b")  false
'''
class Solution(object):
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    return self.dp(s,p)

  def dp(self, s, p):
    path = [[False]*(len(s) + 1) for x in range(len(p) + 1)]
    path[0][0] = True

    for i in range(1, len(p) + 1):
      for j in range(1, len(s) + 1):
        if p[i-1] == '?' or p[i-1] == s[j-1]:
          path[i][j] = path[i-1][j-1]
        elif p[i-1] == '*':
          path[i][j] = path[i-1][j] or path[i][j-1]
      self.printp(path)
    return path[len(p)][len(s)]

  def printp(self,path):
    for i in path:
      print i
    print "*"*10
s = Solution()
#print s.isMatch('ab','?*')
#print s.isMatch('ab','?*c')
