# Dynamic Program I

一维动态规划，基础入门


##Question
##### 1. [leetcode][easy]Range Sum Query - Immutable
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```
Note:
>You may assume that the array does not change.  
>There are many calls to sumRange function.

问题分析：
   -  关键在immutable， 不变
   -  sum(i,j) = sum(j) - sum(i)


##### 2.[leetcode][medium]Range Sum Query 2D - Immutable
Example:
```
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
```
Note:
>You may assume that the matrix does not change.  
>There are many calls to sumRegion function.  
>You may assume that row1 ≤ row2 and col1 ≤ col2.

问题分析：
  - 还是不变
  - sum(a,b,c,d) = d[c,d] - d[a,d] - d[c,b] + d[a,b]

##### 3.[leetcode][medium]Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

问题分析：
  - 最大连续子数组和，经典问题
  - A[n]
  - local[i] = max(local[i-1]+A[i],A[i])
  - global[i] = max(global[i-1],local[i])

##### 4.[leetcode][medium]Maximum Product Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],  
the contiguous subarray [2,3] has the largest product = 6.
```python
  def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    l = len(nums)
    localmin,localmax = [0]*l,[0]*l
    localmin[0],localmax[0],glo = nums[0],nums[0],nums[0]
    for i in range(1, l):
      localmax[i] = self.maxs(self.maxs(localmax[i-1]*nums[i], nums[i]), localmin[i-1]*nums[i])
      localmin[i] = self.mins(self.mins(localmax[i-1]*nums[i], nums[i]), localmin[i-1]*nums[i])
      glo = localmax[i] if localmax[i] > glo else glo
    return glo
```