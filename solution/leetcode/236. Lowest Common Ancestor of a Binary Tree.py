'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree
'''

import copy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        ok,pseq = self.dfs(root,[],p)
        ok,qseq = self.dfs(root,[],q)
        if len(pseq)>len(qseq):
            pseq,qseq=qseq,pseq
        for i in range (1,len(pseq)):
            if pseq[i]!=qseq[i]:
                return pseq[i-1]
        if len(qseq)>len(pseq):
            return qseq[len(pseq)-1]
        return None
    def dfs(self,root,seq,target):
        if root == None:
            return False,None
        seq.append(root)
        if root == target:
            # 跟go不同，没有指针；seq的copy只能靠返回值，不能靠形参；幸好python支持多个返回值
            return True,copy.copy(seq)
        ok,ans = self.dfs(root.left,seq,target)
        if ok:
            return True,ans
        ok,ans = self.dfs(root.right,seq,target)
        if ok:
            return True,ans
        # 跟go不同；python slice 如果想缩容，需要使用内置方法，slice是原来序列的拷贝
        seq.remove(seq[-1])
        return False,None

s = [1,2,3,4,5,6]
s.append(99)
s.append(98)
s = s[:-1]
s[1]=10
print s,s

def modifyseq(seq,seq2):
    seq2 = copy.copy(seq)
    #函数内对形参做修改是没有用的，ide提示了，说是local variable

x = []
modifyseq(s,x)
print x