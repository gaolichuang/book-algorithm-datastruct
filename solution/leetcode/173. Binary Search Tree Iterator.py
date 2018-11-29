'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        r = root
        while r != None:
            self.stack.append(r)
            r = r.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)>0

    def next(self):
        """
        :rtype: int
        """
        # 遍历过程维护stack关系
        x = self.stack[-1]
        r = x.val
        self.stack = self.stack[:(len(self.stack)-1)]
        if x.right != None:
            x = x.right
            while x != None:
                self.stack.append(x)
                x = x.left
        return r

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())