'''
N-Queens My Submissions Question
The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
    There exist two distinct solutions to the 4-queens puzzle:

    [
    [".Q..",  // Solution 1
    "...Q",
    "Q...",
    "..Q."],

    ["..Q.",  // Solution 2
    "Q...",
    "...Q",
    ".Q.."]
    ]
'''
import copy
class Solution(object):
  def solveNQueens(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    q = range(n)
    rets = []
    self.dfs(q,[],rets)
    return rets
  def solvenum(self,n):
    self.dfsnum(range(n), [])
    num = self.num
    self.num = 0
    return num
  def __init__(self):
    self.num = 0

  def dfsnum(self,q,ret):
    if len(ret) == len(q):
      self.num += 1
    for i in range(len(q)):
      if i in ret:
        continue
      if ret and abs(ret[-1] - i) == 1:
        continue
      ret.append(i)
      self.dfsnum(q,ret)
      ret.pop()

  def dfs(self,q,ret,rets):                                
    if len(ret) == len(q):
      que = [['.']*len(q) for x in range(len(q))]
      for i in range(len(ret)):
        que[ret[i]][i] = 'Q'
      value = []
      for k in que:
        value.append(''.join(k))
      rets.append(value)
      return
    for i in range(len(q)):
      if i in ret:
        continue
      if ret and abs(ret[-1] - i) == 1:
        continue
      ret.append(i)
      self.dfs(q,ret,rets)
      ret.pop()

s = Solution()
#print s.solveNQueens(9)
for i in range(15):
  print i,s.solvenum(i)
