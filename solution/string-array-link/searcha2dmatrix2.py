'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

    Consider the following matrix:

    [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]
    Given target = 5, return true.

    Given target = 20, return false.
'''
class Solution(object):
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix: return False
    lr = len(matrix)
    lw = len(matrix[0])
    print lr,lw
    i,j = 0, lw-1
    while i < lr and j >= 0:
      if target > matrix[i][j]:
        i += 1
      elif target < matrix[i][j]:
        j -= 1
      else:
        print i,j
        return True
    return False
a=[
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]
b=[[-5]]
s = Solution()
#print s.searchMatrix(a,20)
print s.searchMatrix(b,-5)
