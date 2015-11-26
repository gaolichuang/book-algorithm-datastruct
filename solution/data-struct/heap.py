class HeapMin(object):
  def __init__(self, s=[], capacity = 5):
    self.s = s
    self.c = capacity
    self._adjust()
  def judge(self, a, b):
    return True if a > b else False
  def _adjustHeap(self, s, m, lens):
    p = m
    j = 2*m + 1
    while j < lens:
      if self.judge(s[j], s[j+1]): j+=1
      if self.judge(s[j], s[p]): break
      s[j],s[p] = s[p],s[j]
      p = j
      j = 2*p + 1

  def _adjust(self):
    i = len(self.s)/2
    while i >= 0:
      self._adjustHeap(self.s, i, len(self.s))
      i -= 1
    while len(self.s) > self.c:
      self.s.pop()

  def add(self, v):
    self.s.append(v)
    idx = len(self.s) - 1
    p = (idx+1)/2 - 1
    while p >= 0:
      if self.judge(self.s[idx],self.s[p]):break
      self.s[p],self.s[idx] = self.s[idx],self.s[p]
      idx = p
      p = (idx+1)/2 - 1
    if len(self.s) > self.c:
      self.s.pop()
      
  def top(self):
    if not self.s: return 0
    return self.s[0]
class HeapMax(HeapMin):
  def judge(self, a, b):
    return True if a < b else False

s = HeapMax([8,3,10,6,5,2,9])
print s.s
s.add(1)
print s.s
