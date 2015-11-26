'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
    Given board =
    [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
   word = "ABCCED", -> returns true,
   word = "SEE", -> returns true,
   word = "ABCB", -> returns false.
'''
class Solution(object):
  def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    self.l = len(board)
    if board:
      self.r = len(board[0])
    visit = []
    for i in range(self.l):
      visit.append([0]*self.r)
    for i in range(self.l):
      for j in range(self.r):
        if board[i][j] != word[0]:
          continue
        visit[i][j] = 1
        if True == self.dfs(board, visit, i,j, word[1:]):
          return True
        visit[i][j] = 0
    return False

  def __init__(self):
    self.r = 0
    self.l = 0

  def dfs(self, board, visit, si, sj, word):
    '''
      si: starti
      sj: startj
    '''
    if len(word) == 0:
      return True
    for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
      ni = si + i
      nj = sj + j
      if ni < 0 or ni >= self.l: continue
      if nj < 0 or nj >= self.r: continue
      if visit[ni][nj] != 0: continue
      if board[ni][nj] != word[0]: continue
      visit[ni][nj] = 1
      if True == self.dfs(board, visit, ni, nj, word[1:]):
        return True
      visit[ni][nj] = 0
    return False
s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print s.exist(board,'ABCCEDE')
