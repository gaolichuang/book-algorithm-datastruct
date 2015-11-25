# Binary Search Tree

二叉树  
二叉查找树，复杂度O(h)， 引来的问题是如何保证树的平衡？  
平衡二叉树：复杂度O(LogN) AVL， 红黑树。。。

涉及到的算法：
 >  DFS/BFS  
 >  各种递归解决方案

二叉树示例
```
      1
     / \
    2   3
       / \
      4   5
前序遍历结果： 1，2，3，4，5
中序遍历结果： 2,1,4,3,5
后序遍历结果： 2，4，5，3，1
定义
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
```


## Question
##### 1. 二叉树前序，中序，后序遍历，递归方式
```
def nlr(root):
  if root:
    print root.val,
    visitTree(root.left)
    visitTree(root.right)
def lrn(root):
  if root:
    visitTree(root.left)
    print root.val,
    visitTree(root.right)
def lrn(root):
  if root:
    visitTree(root.left)
    visitTree(root.right)
    print root.val, # comma means not new line
```


##### 2. 前序中序遍历非递归
```
# base one stack to travel
def visitlnr(root):
  s = []
  while root or s:
    if root:
      s.append(root)
      root = root.left
    else:
      root = s[-1]
      s.pop()
      print root.val,
      root = root.right
def visitnlr(root):
  s = []
  while root or s:
    if root:
      print root.val,
      s.append(root)
      root = root.left
    else:
      root = s[-1].right
      s.pop()
```
reference： [bst travel]  

   [bst travel]: <http://www.gocalf.com/blog/traversing-binary-tree.html>


##### 3. 后序遍历非递归
```
#后序不同于前序和中序的原因是root不能出栈，知道右子树也访问完毕，  使用pre来标记  
#当pre是右子树的情况说明右页访问完， 可以出栈
def visitlrn(root):
  s = []
  pre = None
  while root or s:
    if root:
      s.append(root)
      root = root.left
    elif pre != s[-1].right:
      root = s[-1].right
      pre = None
    else:
      pre = s[-1]
      s.pop()
      print pre.val,
```

#### 4. 层次遍历
```
from collections import deque

def VisitTree_LevelOrder(root):
  if not root: return
  q = deque([root])
  while q:
    root = q.popleft()
    print(root.data)
    if root.left: q.append(root.left)
    if root.right: q.append(root.right)
```
#### 5. 二叉树路径
```
def path(root):
    rets = []
    pathdfs(root,[],rets)
def pathdfs(root, ret, rets):
  if root.left == None and root.right == None:
    ret.append(root)
    import copy
    rets.append(copy.deepcopy(ret))
    for i in ret: print i.val,
    ret.pop()
    return
  if root.left != None:
    ret.append(root)
    pathdfs(root.left, ret, rets)
    ret.pop()
  if root.right != None:
    ret.append(root)
    pathdfs(root.right, ret, rets)
    ret.pop()
```
#### 5. 二叉树高度， 经典递归
```
def treeHeight(root):
  if root == None:
    return 0
  lh = treeHeight(root.left)
  rh = treeHeight(root.right)
  return lh + 1 if lh > rh else rh + 1
```

#### 6. [leetcode][medium]Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.  
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.  
For example, you may serialize the following tree
```
    1
   / \
  2   3
     / \
    4   5
```
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

## TODO
1. AC code
2. Other Questions