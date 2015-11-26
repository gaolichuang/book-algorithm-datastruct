'''
Minimum Path Sum My Submissions Question

Given a m * n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Subscribe to see which companies asked this question

'''
class Solution(object):
  def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    return self.dp(grid)
  def dp(self, grid):
    '''
      dp[i][j] = max(dp[i-1][j],d[[i][j-1]) + grid[i][j]
    '''
    lenm,lenn = len(grid),len(grid[0])
    d = [[0]*(lenn+1) for k in range(lenm+1)]
    import sys
    for i in range(lenn+1): d[0][i] = sys.maxint
    for i in range(lenm+1): d[i][0] = sys.maxint
    for i in range(1,lenm+1):
      for j in range(1,lenn+1):
        if d[i][j-1] ==  sys.maxint and d[i-1][j] ==sys.maxint:
          d[i][j] = grid[i-1][j-1]
          continue
        if d[i-1][j] > d[i][j-1]:
          d[i][j] = grid[i-1][j-1] + d[i][j-1]
        else:
          d[i][j] = grid[i-1][j-1] + d[i-1][j]
    for i in d: print i
    return d[lenm][lenn]
    
s = Solution()
#print s.uniquePaths(3,3)
a=[[1],[2]]
print s.minPathSum(a)
