'''
Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
    Given height = [2,1,5,6,2,3],
    return 10.
'''
class Solution(object):
  def largestRectangleArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height: return 0
    h,s = height,[0]
    h.append(0)
    hs = len(h)
    rect,i = 0,1
    while i < hs:
      if len(s) == 0 or h[i] > h[s[-1]]:
        s.append(i)
        i += 1
      else:
        print h,s,i,(i-s[-1])*h[s[-1]],rect
        t = s[-1]
        s.pop()
        factor = 0 if len(s) == 0 else s[-1] + 1
        rect = (i-factor)*h[t] if rect < (i-factor)*h[t] else rect
        print rect
    return rect
    
s = Solution()
#s.largestRectangleArea([1,5,6])
#print s.largestRectangleArea([2,1,5,6,2,3])
#print s.largestRectangleArea([2,1,2])
print s.largestRectangleArea([0,3,2,5])
