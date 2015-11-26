'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

========
max[i][j] = min(max[i-1][j-1], max[i-1][j], max[i][j-1]) + 1  if maxtrix[i][j] == 1
            0 if maxtrix[i][j] == 0
'''
class Solution(object):
  def mins(self, x, y):
    return x if x < y else y
  def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix: return 0
    lr,lw = len(matrix),len(matrix[0])
    gmax = 0
    d = [[0]*(lw+1) for i in range(lr+1)]
    for i in range(1, lr+1):
      for j in range(1, lw+1):
        if matrix[i-1][j-1] == '0':
          d[i][j] = 0
          continue 
        d[i][j] = self.mins(self.mins(d[i-1][j-1], d[i-1][j]),d[i][j-1])+1
        gmax = d[i][j] if d[i][j] > gmax else gmax
    for i in d: print i 
    return gmax*gmax

s = Solution()
a=[
"10100",
"10111",
"11111",
"10010"
]
b=["0"]
print s.maximalSquare(b)
