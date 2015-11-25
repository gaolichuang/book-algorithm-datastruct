# Stack

stack是一个无序顺序表，只不过规定了元素进入和离开的方式



## Question
##### 1. [Leetcode][Easy] MinStack
    
问题分析
  - O(1)的时间获得栈中最小值
  - 方法： 除了element数组外，在维持一份min element数组， push pop操作同步进行， min则是stack top元素

##### 2. [Leetcode][Easy] Implement Stack using Queues
Implement the following operations of a stack using queues.  
push(x) -- Push element x onto stack.  
pop() -- Removes the element on top of the stack.  
top() -- Get the top element.  
empty() -- Return whether the stack is empty.  
    
问题分析
  - push: O(n)，pop: O(1)，top: O(1)
  - push: O(1)，pop: O(n)，top: O(n)


##### 3. [Leetcode][Hard] Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.  
For example,  
Given height = [2,1,5,6,2,3],  
return 10.
    
问题分析
  - 如何能以更小的代价找到正方形的左边和右边

##### 4. [Leetcode][Hard] Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.  
For example,   
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

问题分析
  - 找到水槽的左边和右边
## TODO
1. AC code
2. Other Questions