'''
Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
    Given [10, 9, 2, 5, 3, 7, 101, 18],
    The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

    Your algorithm should run in O(n2) complexity.

    Follow up: Could you improve it to O(n log n) time complexity?
'''
class Solution(object):
  def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    l = len(nums)
    longs = [1]*l
    longs[0] = 1
    rmax = 1
    for i in range(0,l):
      maxs = 1
      for j in range(i):
        if nums[j] >= nums[i]:
          continue
        maxs = longs[j] + 1 if longs[j] + 1 > maxs else maxs
      longs[i] = maxs
      rmax = longs[i] if longs[i] > rmax else rmax
    print nums
    print longs
    return rmax
s = Solution()
print s.lengthOfLIS([10,9,2,5,3,7,101,18])
print s.lengthOfLIS([2,2,2])
