'''
Generate Parentheses My Submissions Question
Total Accepted: 67836 Total Submissions: 198523 Difficulty: Medium
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''
def solution(n):
    dfs(n,n,[])

def dfs(left, right, ret):
    if left == 0 and right == 0:
      print ''.join(ret)
      return
    if left > 0 and left <= right:
        ret.append('(')
        left = left - 1
        dfs(left, right, ret)
        left = left + 1
        ret.pop()
    if right > 0:
        ret.append(')')
        right = right - 1
        dfs(left, right, ret)
        right = right + 1
        ret.pop()

solution(3)
