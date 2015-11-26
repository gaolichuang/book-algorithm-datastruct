'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,
       1
      / \
     2   3
Return 6.
'''
# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

import sys
class Solution(object):
  def __init__(self):
    self.vmax = -sys.maxint
  def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.dfs(root)
    return self.vmax
  def dfs(self, root):
    if root == None: return 0
    v = root.val
    rmax,lmax = -sys.maxint,-sys.maxint
    if root.left is not None:
      lmax = self.dfs(root.left)
      if lmax > 0:
        v += lmax
    if root.right is not None:
      rmax = self.dfs(root.right)
      if rmax > 0:
        v += rmax
    if v > self.vmax:
      self.vmax = v
    return self.maxs(root.val, self.maxs(a,b))
  def maxs(self, a,b):
    return a if a > b else b

