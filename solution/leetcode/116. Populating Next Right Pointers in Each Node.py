'''
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL

'''


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        queue = [root] # 队列 + 初始化
        while len(queue)>0:
            num = len(queue)
            pre = None
            for i in range (num):
                if pre != None:
                    pre.next = queue[i]
                pre=queue[i]
                if queue[i].left != None:
                    queue.append(queue[i].left)
                if queue[i].right != None:
                    queue.append(queue[i].right)
            # list支持切片
            queue = queue[num:]
if __name__ == '__main__':
    # python一切都是指针
    x = TreeLinkNode(1)
    x.left = TreeLinkNode(2)
    x.right = TreeLinkNode(3)
    solution = Solution()
    print solution.connect(x)