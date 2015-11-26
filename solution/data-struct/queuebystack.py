class MinStack(object):
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
    self.s1 = MinStack(capacity)
    self.s2 = MinStack(capacity)
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
q = QueueByStack()
q.put(4)
q.put(2)
q.put(3)
q.put(5)
q.pop()
q.put(2)
q.put(1)
print q.s1.s,q.s1.smin,q.s1.smax
print q.s2.s,q.s2.smin,q.s2.smax
