# Hash

Hash是一个比较常用的数据结构，最大优势是可以将CRUD(增删改查)的时间复杂度控制在常亮级别  
当然，这需要有较好的hash函数。一个好的Hash函数可以很大程度上提高程序的整体时间效率和空间效率  
关于hash表的实现，首先key的冲突是无法根本避免的，几种实现方式供参考。
  -  依赖hash函数直接寻址： 这种情况较理想，依赖hash存储空间足够大和较好的hash函数
  -  分离链接：借助链表实现，就是将数据实际存放在与 hash 表存储单元相链接的链表中，而不是 hash 的存储单元中。这种有冲突时就不是O(1)
```
[1] --> [next|data] -->Null
[2] --> Null
[3] --> [next|data] --> [next|data] --> Null
[...]
[N+1] --> [next|data]--> Null
```
  -  开放地址
  -  完全hash表

  [hash functions]  里面有hash函数设计的实现， 下面有译文[哈希函数设计]
   - hash函数按照领域分有
     - 字符串hash：经典字符串常用的Hash函数有：BKDRHash，APHash，DJBHash，JSHash，RSHash，SDBMHash，PJWHash，ELFHash等
     - 加密hash
     - 几何hash
     - 布隆过滤器

其他参考
  - [Perfect Hash Fuction] 完美hash函数
  - [gperf] linux gnu对完美hash函数提供的工具，高度可定制化，大型路由器等都会使用并有优化
  - [GeoHash] 涉及空间索引
  - [一致性hash] 当hash存储空间发生变化避免hash函数全局失效。并在平衡性，单调性，分散性，负载上有优化

   [hash functions]: <http://www.partow.net/programming/hashfunctions>
   [哈希函数设计]: <http://blog.csdn.net/eaglex/article/details/6310727>
   [Perfect Hash Fuction]: <http://blog.csdn.net/chixinmuzi/article/details/1727195>
   [gperf]: <http://www.gnu.org/software/gperf/>
   [GeoHash]: <http://www.cnblogs.com/LBSer/p/3310455.html>
   [一致性hash]: <http://blog.csdn.net/cywosp/article/details/23397179/>

## Question
##### 1. 针对区间范围设计一个高效hash函数， 使得一个区间里的数对应一个hash值
区间不重合:例如
```
<<1, 2>, 65>
<<3, 37>, 75>
<<45, 157>, 12>
<<160, 200>, 23>
<<210, 255>, 121>
```
如果给定一个数78，则输出12，因为78属于范围对<45, 159>

问题分析
  - 方案1： 区间排序， 二分查找，O(logN)复杂度
  - 方案2： 查看区间是否有特点，尝试分桶

##### 2. [Leetcode][Medium] Two Sum
Given an array of integers, find two numbers such that they add up to a specific target number.  
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.  
You may assume that each input would have exactly one solution.  
Input: numbers={2, 7, 11, 15}, target=9   
Output: index1=1, index2=2


问题分析
  - hash

##### 3. [Leetcode][Hard] Max Points on a Line
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line

问题分析
  - 减少重复计算
  - 如何判断三点在一条直线上？斜率无效情况
  - 重复点处理。


## TODO
1. AC code
2. Other Questions