'''
Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
'''
class Solution(object):
  def mins(self, x, y):
    return x if x < y else y
  def maxs(self, x, y):
    return x if x > y else y
 
  def maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix: return 0
    lr,lw = len(matrix),len(matrix[0])
    gmax = 0
    d = [[0]*(lw+1) for d1 in range(lr+1)]
    f = [[0]*(lw+1) for f1 in range(lr+1)]
 
    for i in range(1, lr+1):
      for j in range(1, lw+1):
        if matrix[i-1][j-1] == '0':
          d[i][j],f[i][j] = 0,0
          continue 
        m1r = f[i][j-1] if f[i][j-1] < f[i-1][j] else f[i-1][j]
        m1 = (d[i][j-1]+1) * (m1r+1)
        m2r = d[i-1][j-1] if d[i-1][j] <d[i][j-1] else d[i][j-1]
        m2 = (f[i][j-1]+1)*(m2r+1)
        m3r = f[i][j-1] if f[i][j-1] < f[i-1][j-1] else f[i-1][j-1]
        m3w = d[i-1][j] if d[i-1][j] < d[i-1][j-1] else d[i-1][j-1]
        m3 = (m3r+1)*(m3w+1)
        print m1,m2,m3
        if m1 > m2:
          if m1 > m3:
            d[i][j],f[i][j] = d[i][j-1] + 1,m1r+1
          else:
            f[i][j],d[i][j] = m3r+1,m3w+1
        else:
          if m2 > m3:
            f[i][j],d[i][j] = f[i][j-1] + 1,m2r+1
          else:
            f[i][j],d[i][j] = m3r+1,m3w+1

        gmax = d[i][j]*f[i][j] if d[i][j]*f[i][j] > gmax else gmax
    print "X"*8
    for k in d: print k 
    print "X"*8
    for g in f: print g
    return gmax

s = Solution()
a=[
"10100",
"10111",
"11111",
"10010"
]
b=['11']
print s.maximalRectangle(a)
