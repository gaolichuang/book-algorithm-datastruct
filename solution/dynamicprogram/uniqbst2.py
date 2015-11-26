'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
    Given n = 3, your program should return all 5 unique BST's shown below.

    1         3     3      2      1
    \       /     /      / \      \
      3     2     1      1   3      2
      /     /       \                 \
        2     1         2                 3
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:
      1
     / \
    2   3
       /
      4
       \
        5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
'''
# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def generateTrees(self, n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    rets = []
    rets = self.dfs(1,n)
    for r in rets:
      self.bfs(r)
  def dfs(self, begin, end):
    '''
    return root list
    '''
    if begin > end:
      return [None]
    ret = []
    for i in range(begin, end+1):
      left = self.dfs(begin,i-1)
      right = self.dfs(i+1,end)
      for j in left:
        for k in right:
          root = TreeNode(i)
          root.left,root.right = j,k
          ret.append(root)
    return ret
  def bfs(self, root):
      ret = []
      ret.append(root)
      i = 0
      while i < len(ret):
        cur = ret[i]
        if cur == None or cur.val == -1:
          i += 1
          continue
        if cur.left == None and cur.right == None and i == len(ret) - 1:
          break
        if cur.left == None:
          ret.append(TreeNode(-1))
        else:
          ret.append(cur.left)
        if cur.right == None:
          ret.append(TreeNode(-1))
        else:
          ret.append(cur.right)
        i += 1
      value = []
      for k in ret:
        value.append(k.val)
      print value
s = Solution()
s.generateTrees(3)
