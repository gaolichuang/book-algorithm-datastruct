'''
A robot is located at the top-left corner of a m * n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

'''
class Solution(object):
  def uniquePaths(self, m, n):
    """
      :type m: int
       :type n: int
       :rtype: int
       """
    print self.dfs(1,1,m,n)
    print self.dp(m,n)
  def dfs(self, si, sj, m, n):
    if si == m and sj == n:
      return 1
    left,right = 0,0
    if si < m:
      left = self.dfs(si + 1, sj, m, n)
    if sj < n:
      right = self.dfs(si, sj+1, m, n)
    return left + right
  def dp(self, m, n):
    '''
      dp[i][j] = dp[i-1][j]+d[[i][j-1]
    '''
    lenm,lenn = m,n
    d = [[-1]*(lenn) for k in range(lenm)]
    for i in range(lenn): d[0][i] = 1
    for i in range(lenm): d[i][0] = 1
    for i in range(1,lenm):
      for j in range(1,lenn):
        d[i][j] = d[i-1][j] + d[i][j-1]
    return d[lenm-1][lenn-1]
    
s = Solution()
#print s.uniquePaths(3,3)
print s.uniquePaths(1,1)
