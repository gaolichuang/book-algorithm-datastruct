'''
Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''
class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    g = []
    count = 0
    for i in grid: g.append(list(i))
    for i in range(len(g)):
      for j in range(len(g[0])):
        if g[i][j] == '0':
          self.dfs(g,i,j,len(g),len(g[0]))
          count += 1
    return count

  def dfs(self, g, i, j, lr, lw):
    if i < 0 or i >= lr or j < 0 or j >= lw or g[i][j] != '1': return
    g[i][j] = '0'
    self.dfs(g,i+1,j,lr,lw)
    self.dfs(g,i,j-1,lr,lw)
    self.dfs(g,i-1,j,lr,lw)
    self.dfs(g,i,j+1,lr,lw)
