'''
Shortest Palindrome
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:
Given "aacecaaa", return "aaacecaaa".
Given "abcd", return "dcbabcd".
'''
class Solution(object):
  def ispal(self, s, start, end):
    i,j = start,end
    while i < j:
      if s[i] != s[j]:
        return False
      i,j = i+1,j-1
    return True

  def shortestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if not s:return 0
    ls = len(s)
    maxl = 0
    i = ls - 1
    while i >= 0:
      if self.ispal(s,0,i):
        maxl = i + 1 if i + 1 > maxl else maxl
      i -= 1
    return ''.join(reversed(list(s[maxl:]))) + s
s = Solution()
print s.shortestPalindrome('aacecaaa')


