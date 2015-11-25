# Queue

Queue是一个无序顺序表，先入先出

说明：先入先出的结构就应该能想到队列以及跟队列相关的各种操作算法

## Question
##### 1. [Leetcode][Easy] Implement Queue using Stacks	
    
问题分析
  - 在stack中有个问题是用Queue来实现Stack，这道题目反过来， 但更经典，可以保证inqueue，dequeue都是O(1)的
  - 两个Stack描述Queue， S1，S2， 入队则S1 push， 出对则S2 pop， 当S1 full or S2 empty的时候， 触发S1 pop到S2的操作

##### 2. [Leetcode][Easy] MinQueue/MaxQueue
要求O(1)的时间获得队列中最值
问题分析
  - MinStack ==> Two Stack implement Queue ==> MinQueue
  - 有些时候需要能想到这个解法， 如下面的题目

##### 3. [Leetcode][Hard] Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.  
For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
```
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```
Therefore, return the max sliding window as [3,3,5,5,6,7].

问题分析
  - 这个题目方法很多， 比如线段树， 最主要的目的是减少重复计算
  - 还有一个方法，就是问题2，滑动窗口实质上是队列， 问题就是用更小代价来得到队列的最值
  - AC代码参看solution中


## TODO
1. AC code
2. Other Questions