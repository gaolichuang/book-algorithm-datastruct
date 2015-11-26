'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
    Given n = 3, there are a total of 5 unique BST's.

     1        3     3      2      1
     \       /     /      / \      \
      3     2     1      1   3      2
     /     /       \                 \
    2     1         2                 3

'''
class Solution(object):
  def numTrees(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0: return 0
    ln = n
    d = [0]*(ln+1)
    d[0],d[1] = 1,1
    for i in range(1,ln):
      for j in range(i+1):
        d[i+1] += d[j]*d[i-j]
    print d
    return d[n]
s = Solution()
s.numTrees(4)
    

