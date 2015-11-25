# Linklist/DoubleLinklist

内存中存储不连续，有后向/前向指针。


## Question
##### 1. 单链表环的判断和位置

    
问题分析
  - 如何判断单链表存在环？
  - 找到环的入口位置

##### 2. [leetcode][hard]Copy List with Random Pointer My Submissions Question
>A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.   
Return a deep copy of the list.



    
问题分析
  - 随机指针， 需要找方式来实现copy后的链表对应关系



##### 3.[LeetCode][easy] Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.  
Example  
Given: 1 –> 2 –> 6 –> 3 –> 4 –> 5 –> 6, val = 6  
Return: 1 –> 2 –> 3 –> 4 –> 5  
```
/**
 * 递归实现
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
	if (head == null) {
		return null;
	}
	if (head.val == val){
		head = removeElements(head.next, val);
	} else {
		head.next = removeElements(head.next, val);
	}
	return head;
    }
}
```