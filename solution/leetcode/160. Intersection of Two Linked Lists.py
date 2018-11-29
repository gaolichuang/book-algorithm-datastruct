'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.
Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        if p == None:
            return None
        while p.next != None:
            p = p.next
        p.next = headA
        x = self.detectCycle(headB)
        p.next = None
        return x
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow,fast = head,head
        while fast != None and slow != None:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return None
            fast = fast.next
            if fast == slow:
                #可以通过运算得到，1step 2step交汇后，再找一个从head走，第一个相遇位置就是了。
                x = head
                while x != slow:
                    x = x.next
                    slow = slow.next
                return x
        return None