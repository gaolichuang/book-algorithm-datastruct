'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
  [2],
  [3,4],
  [6,5,7],
  [4,1,8,3]
]
  The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

  Note:
  Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
class Solution(object):
  def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    import sys
    tt = triangle
    if len(tt) == 1:
      return tt[0][0]
    last,cur = tt[0],[]
    for i in range(1,len(tt)):
      cur = []
      for j in range(len(tt[i])):
        lt = sys.maxint
        if j >0:
          lt = last[j-1]
        try:
          t = last[j]
        except:
          t = sys.maxint
        if lt > t:
          cur.append(t + tt[i][j])
        else:
          cur.append(lt + tt[i][j])
      print last,cur,t,lt
      last = cur
    minv = sys.maxint
    for v in cur:
      if v < minv:
          minv = v
    return minv
s = Solution()
t=[
  [2],
  [3,4],
  [6,5,7],
  [4,1,8,3]
]
a = [[-1],[-2,-3]]
b = [ [-1],
      [3,2],
      [-3,1,-1]]
print s.minimumTotal(a)
