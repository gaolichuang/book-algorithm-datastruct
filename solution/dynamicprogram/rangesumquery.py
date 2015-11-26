'''
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''
class NumArray(object):
  '''
    sum(i,j) = sum(j) - sum(i)
  '''
  def __init__(self, nums):
    """
    initialize your data structure here.
    :type nums: List[int]
    """
    self.d = []
    if not nums: return
    self.lens = len(nums)
    self.d = [0]*(self.lens+1)
    self.d[0] = 0
    self.d[1] = nums[0]
    for i in range(1,self.lens): self.d[i+1] = self.d[i] + nums[i]
    print self.d

  def sumRange(self, i, j):
    """
    sum of elements nums[i..j], inclusive.
    :type i: int
    :type j: int
    :rtype: int
    """
    return self.d[j+1] - self.d[i]

# Your NumArray object will be instantiated and called as such:
nums = [1,2,3,4]
numArray = NumArray(nums)
#numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
