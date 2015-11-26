'''
Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Subscribe to see which companies asked this question


1. from begin to end, if s[i] == ")"   and s[i-d[i-1]-1] == "(": have found a pair, add 2
2. then combine two neigh to one ==> if d[i-d[i-1]-2   avaliable and not 0
'''
class Solution(object):
  def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s: return 0
    l = len(s)
    d = [0]*l
    maxs = 0
    for i in range(1,l):
      if s[i] == ')' and i-d[i-1]-1 >=0 and s[i-d[i-1]-1] == '(':
        d[i] = 2 + d[i-1]
        if i - d[i-1]-2 > 0 and d[i-d[i-1]-2] != 0:
            d[i]+=d[i-d[i-1]-2]
      maxs = d[i] if d[i] > maxs else maxs

    print d
    return maxs
s = Solution()
print s.longestValidParentheses('(()))())(')
#print s.longestValidParentheses(')()())')
#print s.longestValidParentheses(')(())(())()())')
#print s.longestValidParentheses('()()')
