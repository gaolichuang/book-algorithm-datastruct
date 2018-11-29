'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
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