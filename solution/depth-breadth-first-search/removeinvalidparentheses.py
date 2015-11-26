'''
Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).
Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''
class Solution(object):
  def __init__(self):
    self.dup = set()
  def removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
  def bfs(self, s):
    import Queue
    mq = Queue.Queue()
    mq.put(s)
    tlevel,ret = 0,[]
    ret = []
    while not mq.empty():
      v = mq.get()
      if len(v) < tlevel:
        break
      if self.validparentheses(v):
        ret.append(v)
        tlevel = len(v)
      else:
        for i in range(len(v)):
          if v[i] != '(' and v[i] != ')':
            continue
          t = v[:i] + v[i+1:]
          if t not in self.dup:
            self.dup.add(t)
            mq.put(t)
    return ret

        

  def validparentheses(self,s):
    i,ln,rn = 0,0,0
    while i < len(s):
      if s[i] == '(':
        ln += 1
      elif s[i] == ')':
        rn += 1
      i += 1  
      if rn > ln: return False
    return rn == ln
  def dfs(self, s, i, ret):
    if len(s) == i:
      rv =  ''.join(ret)
      if self.validparentheses(rv) and rv not in self.dup:
        print rv
        self.dup.add(rv)
      return
    if s[i] == '(' or s[i] == ')':
      self.dfs(s,i+1,ret)
      ret.append(s[i])
#    ret.append(i)
      self.dfs(s,i+1,ret)
      ret.pop()
    else:
      ret.append(s[i])
      self.dfs(s,i+1,ret)
      ret.pop()

s = Solution()
print s.bfs('()())()')
s.bfs('(a)())()')
#s.dfs('()())()',[])
#s.dfs('(a)())()',0,[])
#print s.validparentheses('(a)(()))')
