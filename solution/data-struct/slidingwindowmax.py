'''
Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
    Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7
    Therefore, return the max sliding window as [3,3,5,5,6,7].

    Note: 
    You may assume k is always valid, ie: 1 <=  k <=  input array's size for non-empty array.
    Follow up:
    Could you solve it in linear time?

    Hint:

    How about using a data structure such as deque (double-ended queue)?
    The queue size need not be the same as the window s size.
    Remove redundant elements and the queue should store only elements that need to be considered.
'''

class MStack(object):
  def __init__(self, capacity = 10):
    self.s = []
    self.smin = []
    self.smax = []
    self.c = capacity
  def push(self,v):
    self.s.append(v)
    m = v
    m = self.smin[-1] if len(self.smin) > 0 and self.smin[-1] < v else m
    self.smin.append(m)
    m = v
    m = self.smax[-1] if len(self.smax) > 0 and self.smax[-1] > v else m
    self.smax.append(m)
  def pop(self):
    self.s.pop()
    self.smin.pop()
    self.smax.pop()
  def mins(self):
    return self.smin[-1]
  def maxs(self):
    return self.smax[-1]
  def full(self):
    return len(self.s) >= self.c
  def empty(self):
    return len(self.s) <= 0
  def top(self):
    return self.s[-1]

class QueueByStack(object):
  def __init__(self, capacity = 10):
    self.s1 = MStack(capacity)
    self.s2 = MStack(capacity)
  def put(self,v):
    if self.s1.full():
      self.flush()
    self.s1.push(v)
  def pop(self):
    if self.s2.empty():
      self.flush()
    self.flush
    self.s2.pop()
  def flush(self):
    while not self.s1.empty():
      self.s2.push(self.s1.top())
      self.s1.pop()
  def maxs(self):
    import sys
    ma = -sys.maxint
    if not self.s1.empty():
      ma = self.s1.maxs() if self.s1.maxs() > ma else ma
    if not self.s2.empty():
      ma = self.s2.maxs() if self.s2.maxs() > ma else ma
    return ma

class Solution(object):
  def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums or len(nums) < k -1 :return []
    first = k
    queue = QueueByStack(k+1)
    for i in range(first): queue.put(nums[i])
    print queue.s1.s,queue.s1.smax
    ret = []
    ret.append(queue.maxs())
    while first < len(nums):
      queue.put(nums[first])
      queue.pop()
      ret.append(queue.maxs())
      first += 1
    return ret
s = Solution()
print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)

