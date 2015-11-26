'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''
class Solution(object):
  def restoreIpAddresses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    if len(s) > 12 or len(s) < 4:
      return []
    rets = []
    self.dfs(s, [], rets)
    return rets

  def dfs(self, s, ans, rets):
    if len(ans) == 4 and len(s) == 0:
      val = '.'.join(ans)
      if val not in rets:
        rets.append(val)
      return
    for i in range(3):
      try:
        value = s[:i+1]
        if value[0] == '0' and len(value) > 1:
          continue
        if int(value) < 256:
          ans.append(value)
          self.dfs(s[i+1:], ans, rets)
          ans.pop()
      except:
        pass

s = Solution()
#print s.restoreIpAddresses('25525511135')
#print s.restoreIpAddresses('0000')
print s.restoreIpAddresses("010010")
