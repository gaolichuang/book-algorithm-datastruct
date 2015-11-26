# Sort II

跟sort有关的一些题目

### Question

##### 1.[leetcode][medium]Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

问题分析：
  - 举个例子：要比较3和34的先后位置，可以比较334和343的大小，而343比334大，所以34应当在前。  
  - 这样，有了比较两个数的方法，就可以对整个数组进行排序。然后再把排好序的数拼接在一起就好了。

```python
  def largestNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    ret = sorted(nums,
    		cmp = lambda x,y : 
    				cmp(int(str(y) + str(x)),
    					int(str(x)+str(y))))
    print ret
    retv = ''
    i = 0
    while i < len(ret) and ret[i] == 0: i += 1
    while i < len(ret):
      retv += str(ret[i])
      i += 1
    if retv == '': retv = '0'
    return retv        

```