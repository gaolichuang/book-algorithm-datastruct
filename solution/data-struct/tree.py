'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

      1
     / \
    2   3
       / \
      4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
def visitTree(root,order):
  if root:
    if order == 'NLR': print root.val,
    visitTree(root.left, order)
    if order == 'LNR': print root.val,
    visitTree(root.right, order)
    if order == 'LRN': print root.val,
def nlr(root):
  visitTree(root,'NLR')
  print '#'*8
def lnr(root):
  visitTree(root,'LNR')
  print '#'*8
def lrn(root):
  visitTree(root,'LRN')
  print '#'*8
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
def path(root):
    rets = []
    pathdfs(root,[],rets)
def pathdfs(root, ret, rets):
  if root.left == None and root.right == None:
    ret.append(root)
    import copy
    rets.append(copy.deepcopy(ret))
    for i in ret: print i.val,
    print "*"*8
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


def treeHeight(root):
  if root == None:
    return 0
  lh = treeHeight(root.left)
  rh = treeHeight(root.right)
  return lh + 1 if lh > rh else rh + 1

class Codec:
  def serialize(self, root):
    """Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    rlist = [root]
    i = 0
    while True:
      if i >= len(rlist): break
      if rlist[i] == None:
        i += 1
        continue
      rlist.append(rlist[i].left)
      rlist.append(rlist[i].right)
      i += 1
    s = ''
    for i in rlist:
      if i == None:
        s += '#'
      else:
        s += str(i.val)
    return s

  def deserialize(self, data):
    """Decodes your encoded data to tree.
    :type data: str
    :rtype: TreeNode
    """
    if not data: return None
    if data and data[0] == '#': return None
    root = TreeNode(data[0])
    rlist = [root]
    p,c = 0,1
    while c < len(data):
      if data[c] != '#':
        rlist.append(TreeNode(data[c]))
      else:
        rlist.append(None)
      if data[c+1] != '#':
        rlist.append(TreeNode(data[c+1]))
      else:
        rlist.append(None)
      c += 2
      if rlist[p] != None:
        rlist[p].left,rlist[p].right = rlist[-2],rlist[-1]
      p += 1
    return rlist[0]
codec = Codec()
root = codec.deserialize('123##45####')
#nlr(root)
#print treeHeight(root)
#print codec.serialize(codec.deserialize('123##45####'))
#print codec.serialize(codec.deserialize('123##45####'))
#lnr(root)
#visitlnr(root)
#nlr(root)
#visitnlr(root)
path(root)
#lrn(root)
#visitlrn(root)
