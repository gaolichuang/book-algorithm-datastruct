'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:






We should return its max depth, which is 3.



Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.

'''

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # nil...
        if root == None:
            return 0
        if len(root.children)==0:
            return 1
        # max方法和 list travel方式
        return max(self.maxDepth(node) for node in root.children) + 1
        '''
        ans = 0
        # travel list
        for c in root.children:
            ans = max(ans,self.maxDepth(c))
        return ans+1
        '''
if __name__ == '__main__':
    solution = Solution()
    print solution.maxDepth(None)