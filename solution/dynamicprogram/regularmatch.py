'''
Regular Expression Matching My Submissions Question

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

    Some examples:
    isMatch("aa","a")  false
    isMatch("aa","aa")  true
    isMatch("aaa","aa")  false
    isMatch("aa", "a*")  true
    isMatch("aa", ".*")  true
    isMatch("ab", ".*")  true
    isMatch("aab", "c*a*b")  true
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
    # init
    for i in range(len(p)):
      if p[i] == '*':
        path[i+1][0] = path[i-1][0]
    for i in range(1, len(p) + 1):
      for j in range(1, len(s) + 1):
        if p[i-1] == '.' or p[i-1] == s[j-1]:
          path[i][j] = path[i-1][j-1]
        elif p[i-1] == '*':
          path[i][j] = path[i-2][j] or path[i-1][j]
          if p[i-2] == s[j-1] or p[i-2] == '.':
            path[i][j] = path[i][j] or path[i-1][j-1] or path[i][j-1]
      self.printp(path)
    return path[len(p)][len(s)]
  def printp(self,path):
    for i in path:
      print i
    print "*"*10
          
s = Solution()
#print s.isMatch("aaaa", "a*")
#print s.isMatch("aaa", "a*a")
#print s.isMatch("aaa", "ab*a*c*a")
print s.isMatch("aab", "c*a*b")
#print s.isMatch("abcd", "d*")
