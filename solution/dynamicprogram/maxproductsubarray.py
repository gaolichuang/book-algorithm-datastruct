'''
Maximum Product Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
    the contiguous subarray [2,3] has the largest product = 6.

    Subscribe to see which companies asked this question

    ============
    max_copy[i] = max_local[i]
    max_local[i + 1] = Max(Max(max_local[i] * A[i], A[i]),  min_local * A[i])

    min_local[i + 1] = Min(Min(max_copy[i] * A[i], A[i]),  min_local * A[i])
'''
class Solution(object):
  def maxs(self, x, y):
    return x if x > y else y
  def mins(self,x,y):
    return x if x < y else y

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
    print localmin,localmax
    return glo
s = Solution()
#print s.maxProduct([2,3,-2,4])
#print s.maxProduct([-3,-4])
print s.maxProduct([-3,-2,-4])

