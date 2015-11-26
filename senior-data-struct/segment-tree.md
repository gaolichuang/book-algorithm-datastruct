# Segment Tree

线段树，一般涉及到区间的问题会用线段树解决

解决问题示例：  
> 一个经常改变的区间， 求[i,j]的最值  
> 更新节点 or 成段更新， 区间求和，区间统计

```
                          [1,10]
                   /                  \
               [1,5]                   [5,10]
            /      \                 /      \
        [1,3]      [3,5]         [5,7]      [7,10]
        /  \        /  \         /  \        /   \
    [1,2] [2,3]  [3,4] [4,5] [5,6]  [6,7] [7,8]  [8,10]
                                                 /     \   
                                              [8,9]   [9,10]  
```
特点：
> 线段树是一颗二叉树，T(a,b) 表示区间[a,b]， 记为L  
> 如果L > 1 : 则[a, (a+b)/2]为T的左孩子 [(a+b)/2, b]为T的右孩子
> 如果L == 1: T为叶子节点

```python
结构定义， build， insert， delete 方法如下
class SegNode(object):
  def __init__(self, l, r):
    self.left = l
    self.right = r
    self.cover = 0
    self.leftchild = None
    self.rightchild = None

class SegTree(object):
  def __init__(self, s, e):
    self.start = s
    self.end = e
    self.root = self.build(s, e)
  def build(self, l, r):
    root = SegNode(l, r)
    if l + 1 < r:
      mid = (r + l) >> 1
      root.leftchild = self.build(l, mid)
      root.rightchild = self.build(mid, r)
    return root
  def insert(self, c, d, root):
    '''
      insert one segment [c,d]
    '''
    if c <= root.left and d >= root.right:
      root.cover += 1
    else:
      if c < (root.left + root.right)/2:
        self.insert(c,d,root.leftchild)
      if d > (root.left + root.right)/2:
        self.insert(c,d,root.rightchild)
  def delete(self, c, d, root):
    if c <= root.left and d >= root.right:
      root.cover -= 1
    else:
      if c < (root.left + root.right)/2:
        self.delete(c,d,root.leftchild)
      if d > (root.left + root.right)/2:
        self.delete(c,d,root.rightchild)
  def count(self, root):
    '''
      statistic how long of all segment
    '''
    m,n = 0,0
    if root.cover > 0:
      return root.right - root.left
    elif root.right - root.left == 1:
      return 0
    m = self.count(root.leftchild)
    n = self.count(root.rightchild)
    return m + n
```


## Question
##### 1. x轴上有若干条线段，求线段覆盖的总长度，即S1+S2+...+SN的长度。
```
    S1       S2                 S3           S4
|------                         ------
|    ------------    ----------------------------
|----------------------------------------------------------
```


##### 2. [leetcode][medium]Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]  

sumRange(0, 2) -> 9  
update(1, 2)  
sumRange(0, 2) -> 8  
Note:  
>The array is only modifiable by the update function.  
>You may assume the number of calls to update and sumRange function is distributed evenly.  


## TODO
1. AC code
2. Other Questions
