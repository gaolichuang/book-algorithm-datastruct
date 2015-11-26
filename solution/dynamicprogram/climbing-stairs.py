'''
Climbing Stairs My Submissions Question
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

f[i] = f[i-1] + f[i-2]
'''
class Solution(object):
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    ret = []
    ret.append(1)
    ret.append(2)
    if n < 3:
      return ret[n-1]
    for i in range(2,n):
      ret.append(ret[i-1] + ret[i-2])
    return ret[n-1]
s = Solution()
print s.climbStairs(5)
