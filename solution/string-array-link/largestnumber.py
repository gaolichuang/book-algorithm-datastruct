'''
Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.
'''
class Solution(object):
  def largestNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    ret = sorted(nums, cmp=lambda x,y : cmp(int(str(y) + str(x)), int(str(x)+str(y))))
    print ret
    retv = ''
    i = 0
    while ret[i] == 0: i += 1
    while i < len(ret):
      retv += str(ret[i])
      i += 1
    if retv == '': retv = '0'
    return retv

s = Solution()
#print s.largestNumber([3,30,34,5,9])
print s.largestNumber([0,1,2,3,4,5,6,8])
