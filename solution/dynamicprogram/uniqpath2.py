'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
    There is one obstacle in the middle of a 3x3 grid as illustrated below.

    [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
    The total number of unique paths is 2.

    Note: m and n will be at most 100.

'''
class Solution(object):
  def uniquePathsWithObstacles(self, obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    return self.dp(obstacleGrid)
  def dp(self, grid):
    '''
      dp[i][j] = dp[i-1][j]+d[[i][j-1]
    '''
    lenm = len(grid)
    lenn = len(grid[0])
    if grid[0][0] == 1 or grid[lenm-1][lenn-1] == 1: return 0
    d = [[-1]*(lenn) for k in range(lenm)]
    d[0][0] = 1
    for i in range(1,lenn): d[0][i] = d[0][i-1] if grid[0][i] != 1 else 0
    for i in range(1,lenm): d[i][0] = d[i-1][0] if grid[i][0] != 1 else 0
    for i in d: print i
    for i in range(1,lenm):
      for j in range(1,lenn):
        if grid[i][j] == 1:
          d[i][j] = 0
        else:
          d[i][j] = d[i-1][j] + d[i][j-1]
    for i in d: print i
    return d[lenm-1][lenn-1]
    
s = Solution()
#print s.uniquePaths(3,3)
a = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
b = [[0,0],[1,1],[0,0]]
c = [[0],[0]]
print s.uniquePathsWithObstacles(c)
