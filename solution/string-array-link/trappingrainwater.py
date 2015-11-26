'''
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
    Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

    The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
'''
class Solution(object):
  def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:return 0
    h,lh =  height,len(height)
    i,j,trap = 0,lh-1,0
    li,lj = 0,0
    while i < j:
      if h[i] > h[j]:
        lj = h[j] if h[j] > lj else lj
        trap += lj - h[j]
        j -= 1
      else:
        li = h[i] if h[i] > li else li
        trap += li - h[i]
        i += 1
    return trap
s = Solution()
print s.trap([6,4,5,3,2,6])
print s.trap([4,2,3])
