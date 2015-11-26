'''
Maximum Subarray My Submissions Question

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
sample: [-2,1,-3,4,-1,2,1,-5,4]
max sum is [4,-1,2,1]  sum is 6
'''
class Solution(object):
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    l = len(nums)
    local = [0]*l
    glo = [0]*l
    local[0],glo[0] = nums[0],nums[0]
    for i in range(1,l):
      if 0 > local[i-1]:
        local[i] = nums[i]
      else:
        local[i] = local[i-1] + nums[i]
      if glo[i-1] < local[i]:
        glo[i] = local[i]
      else:
        glo[i] = glo[i-1]
    print local
    print glo
    return glo[l-1]
s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
