'''
House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

'''
class Solution(object):
  def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    money = []
    if len(nums) == 1:
      return nums[0]
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

