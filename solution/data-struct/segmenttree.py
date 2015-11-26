'''
segment tree
'''
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

