# Array
内存中连续存储块， 基础数据结构。

Array和之后的ListLink可以表示动态集和静态集。

关于动态集和静态集的操作如下



| 名称   |      结构分类      |  插入 | 删除 | 查找 |
|----------| :-------------: | ------: | ------: | ------: |
| 线性表 |  顺序表 - 有序表 | O(N) |O(N) |O(logN) |
|       |  顺序表 - 无序表 | O(1) |O(N)查找时间 |O(N) |
|       |  链表 - 有序表   | O(N) |O(N) |O(N) |
|       |  链表 - 无序表   | O(1) |O(N) |O(N) |

 - 说明
    - 顺序表-无序表的删除为O(N)为查找时间， 用最后一个元素覆盖，调整长度，不需要移动，则删除时间为常量级
    - 链表-无序表的插入时间O(1) : 插入在表头
 - 其他
   - 一般情况下，不用有序链表，因为无序要好于有序链表
   - 一般情况下也不用链表， 因为无序顺序表和无序链表时间上差不多， 但无序链表的空间消耗大
   - 轻易不要用链表，更不要轻易用有序链表
   - 栈和队列类似无序顺序表，二叉树中这三个操作的复杂度均为O(h)树高，其中插入和删除会影响树的平衡，涉及平衡树内容

## Question
##### 1. [leetcode][Medium]3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
>Note:
>Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
>The solution set must not contain duplicate triplets.
>>    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is: (-1, 0, 1) (-1, -1, 2)
    
问题分析
  -  找到三个数字 sum 为0, 最直接方式三层for循环，时间复杂度是O(n^3)；
  - 优化的方法是先排序， 如果是2sum， 则两个头尾指针可以搞定； 3sum则先固定一个数，2sum这个数的相反数即可。 
  - [k sum solution]这篇文章介绍了通用K SUM问题解法。

   [k sum solution]: <http://tech-wonderland.net/blog/summary-of-ksum-problems.html>

## TODO
1. AC code 3sum
2. Other Questions