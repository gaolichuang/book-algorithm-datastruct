'''
Move Zeroes My Submissions Question
Total Accepted: 31588 Total Submissions: 75279 Difficulty: Easy
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution(object):
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 2: return nums
    n = nums
    i,ln = 0, len(n)
    while i < ln:
      while i < ln and n[i] != 0: i += 1
      j = i + 1
      while j < ln and n[j] == 0: j += 1
      if j < ln: n[i],n[j] = n[j],n[i]
      i += 1
    return nums

s = Solution()
print s.moveZeroes([0,1,0,3,12])
print s.moveZeroes([0,0])

