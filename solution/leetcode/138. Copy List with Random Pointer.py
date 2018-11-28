'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.


'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        # 用来做新旧节点的对应，key是旧节点指针，value是新节点指针
        d = {}
        p = head
        n = RandomListNode(head.label)
        q = n
        d[p]=q
        while p.next != None:
            p = p.next
            q.next = RandomListNode(p.label)
            q = q.next
            d[p]=q
        p = head
        q = n
        while p != None:
            if p.random != None:
                # random替换，新节点的random用对应旧节点对应的新节点替换
                q.random = d[p.random]
            p = p.next
            q = q.next
        return n


if __name__ == '__main__':
    solution = Solution()
    n = RandomListNode(1)
    n.next=RandomListNode(2)
    n.random=n.next
    n.next.random=n.next
    print solution.copyRandomList(n)
