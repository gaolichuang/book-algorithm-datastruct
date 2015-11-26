# Search

查找给定的key是否在集合中，返回True/False or Value  
对于有序集合，可以采用二分，LogN复杂度  


##Question
##### 1. 二分查找

```python
def binarySearch(A, X):
    N = len(A)
    if N == 0:
      return -1
    l = 0
    r = N - 1
    while l < r:
      m = (l + r) // 2
      if A[m] >= X:
        r = m if A[m] == X else m - 1
      else:
        l = m if A[m] == X else m + 1
    if A[l] == X:
      return l
    return -1
```

##### 2. [leetcode][Medium]Find Minimum in Rotated Sorted Array
> Suppose a sorted array is rotated at some pivot unknown to you beforehand.  
> (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).  
> Find the minimum element.  
You may assume no duplicate exists in the array.  

问题分析过程
> 首先假设数组A和B的元素个数都大于k/2，我们比较A[k/2-1]和B[k/2-1]两个元素，  
> 这两个元素分别表示A的第k/2小的元素和B的第k/2小的元素。  
> 这两个元素比较共有三种情况：>、<和=。如果A[k/2-1]<B[k/2-1]，这表示A[0]到A[k/2-1]的元素都在A和B合并之后的前k小的元素中。换句话说，A[k/2-1]不可能大于两数组合并之后的第k小值，所以我们可以将其抛弃。  
证明也很简单，可以采用反证法。假设A[k/2-1]大于合并之后的第k小值，我们不妨假定其为第（k+1）小值。由于A[k/2-1]小于B[k/2-1]，所以B[k/2-1]至少是第（k+2）小值。但实际上，在A中至多存在k/2-1个元素小于A[k/2-1]，B中也至多存在k/2-1个元素小于A[k/2-1]，所以小于A[k/2-1]的元素个数至多有k/2+ k/2-2，小于k，这与A[k/2-1]是第（k+1）的数矛盾。  
> 当A[k/2-1]>B[k/2-1]时存在类似的结论。
> 当A[k/2-1]=B[k/2-1]时，我们已经找到了第k小的数，也即这个相等的元素，我们将其记为m。由于在A和B中分别有k/2-1个元素小于m，所以m即是第k小的数。(这里可能有人会有疑问，如果k为奇数，则m不是中位数。这里是进行了理想化考虑，在实际代码中略有不同，是先求k/2，然后利用k-k/2获得另一个数。)

通过上面的分析，我们即可以采用递归的方式实现寻找第k小的数。此外我们还需要考虑几个边界条件：

如果A或者B为空，则直接返回B[k-1]或者A[k-1]；
如果k为1，我们只需要返回A[0]和B[0]中的较小值；
如果A[k/2-1]=B[k/2-1]，返回其中一个；

##### 3. [leetcode][Hard]Find Minimum in Rotated Sorted Array ||
>  - Follow up for "Find Minimum in Rotated Sorted Array":  
>  - What if duplicates are allowed?  
>  - Would this affect the run-time complexity? How and why? 

Suppose a sorted array is rotated at some pivot unknown to you beforehand.  
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).   
Find the minimum element.   
The array may contain duplicates.

##### 4. [leetcode][Medium]Search a 2D Matrix
>Write an efficient algorithm that searches for a value in an m x n matrix.   
This matrix has the following properties:  
> -  Integers in each row are sorted from left to right.
  - The first integer of each row is greater than the last integer of the previous row.  

For example,
Consider the following matrix:
```
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
```
Given target = 3, return true.

问题分析
   - O(m+n)的时间复杂度解决,A[M][N]
   - 找到入口，从A[0][n-1]出发， 小了向下（说明一整行都小），打了向左（说明从该点向下都大）
   - 
   
##### 5. [G]查询系统中“匹配”的最短单词
> 系统中有a-z组成的单词， query的key也是由a-z组成，最长为7个字符。
> 返回匹配的最短单词。匹配指的无序，并包含query所有字符即可。  
> Sample:   单词 {‘loudly’,'loud','louly'}  
>  如果query 为  ll， 则返回  louly  
> 如果query为 lo 则返回 loud
 - 要求 查询时间为O(1)
 

问题分析：  
  - query match是无序的，只要query的字母在单词中全出现即为 match。找到match中最短的单词
  - 对单词做预处理，排序后，生成每个单词的子集，子集作为key，value为单词本身。
  - {str:set()}结构，每个key对多个value，获得最短的一个存储
  - query来了之后先排序， 然后再dict个查询