class MinStack(object):
  def __init__(self, capacity = 10):
    self.s = []
    self.smin = []
  def push(self,v):
    self.s.append(v)
    m = v
    m = self.smin[-1] if len(self.smin) > 0 and self.smin[-1] < v else m
    self.smin.append(m)
  def pop(self):
    self.s.pop()
    self.smin.pop()
  def mins(self):
    return self.smin[-1]

s = MinStack()
s.push(5)
s.push(3)
s.push(6)
s.push(2)
print s.s,s.smin
print s.mins()
s.pop()
print s.mins()
print s.s,s.smin
