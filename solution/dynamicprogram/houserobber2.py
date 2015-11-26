'''
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution(object):
  def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    max1 = self.rob1(nums[1:])
    max2 = self.rob1(nums[:-1])
    if max1 > max2:
      return max1
    return max2

  def rob1(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    money = []
    if len(nums) == 1: return nums[0]
    money.append(nums[0])
    if len(nums) >= 2:
      nmax = nums[0] if nums[0] > nums[1] else nums[1]
    money.append(nmax)
    if len(nums) == 2:
      return nmax
    for i in range(2, len(nums)):
      if money[i-1] > money[i-2] + nums[i]:
        money.append(money[i-1])
      else:
        money.append(money[i-2] + nums[i])
    return money[-1]

s = Solution()
print s.rob([1,3,4,5,6])

