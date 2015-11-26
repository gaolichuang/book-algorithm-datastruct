'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
    Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

    The number of ways decoding "12" is 2.

failure condition is too much
'''
class Solution(object):
  def __init__(self):
    self.lens = 0
  def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """
#    self.dfs(s,[])
#    return self.lens
    return self.dp(s)
  def dp(self, s):
    if not s: return 0
    if len(s) == 1 and s[0] == '0': return 0
    if len(s) == 1 and s[0] != '0': return 1
    if '00' in s or s[0] == '0': return 0
    for i in range(1,len(s)):
      if s[i] == '0' and s[i-1] > '2':
        return 0
    ret = [1,1]
    for n in range(1, len(s)):
      if s[n-1] == '1' or s[n-1] == '2':
        if s[n-1:n+1] in ['27','28','29']:
          if ret[n-1] > ret[n]:
            ret.append(ret[n-1])
          else:
            ret.append(ret[n])
        elif s[n] == '0':
            ret.append(ret[n-1])
        else:
          ret.append(ret[n-1] + ret[n])
      else:
        ret.append(ret[n])
    print ret
    return ret[len(s)]
  def dfs(self, s, ret):
    if not s:
#      print ret
      self.lens += 1
      return
    if s[0] != '0':
      ret.append(s[:1])
      self.dfs(s[1:],ret)
      ret.pop()
    if (s[0] == '1' or s[0] == '2') and len(s) >1:
      ret.append(s[:2])
      self.dfs(s[2:],ret)
      ret.pop()
s = Solution()

print s.numDecodings("110")
print s.numDecodings("230")
print s.numDecodings("227")
print s.numDecodings("11")
print s.numDecodings("10")
print s.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
#print s.numDecodings("1111111")
#print s.numDecodings("12120102")
