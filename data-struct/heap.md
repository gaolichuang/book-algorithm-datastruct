# Heap

以树的结构，以较小的代价维持最值，可以在O(logN)的时间内删除，插入，O(1)时间得到最值  
涉及大顶堆和小顶堆，具体建堆和调整堆的过程会在堆排序中说明。
下面说下使用场景：
  -  优先级队列
  -  维持一个持续数据流的 TopN

说明：这种数据结构只能在O(1)时间获得最值， 非最值的元素查找时间是O(N)的。

## Question
##### 1. [Leetcode] Find Median from Data Stream 数据流中位数 or n/10个数字
    
问题分析
  - 最大堆和最小堆： 前半部分最小堆， 后半部分最大堆， 堆顶就是中间的两个元素


##### 2.[leetcode][hard]The Skyline Problem

排序+堆， 进入和离开， 进入计算最大值， 离开删掉最大值，调整堆
http://segmentfault.com/a/1190000003786782


## TODO
1. AC code
2. Other Questions