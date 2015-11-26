'''
Additive Number My Submissions Question

Additive number is a positive integer whose digits can form additive sequence.
A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string represents an integer, write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?

'''
class Solution(object):
  def isAdditiveNumber(self, num):
    """
    :type num: str
    :rtype: bool
    """
    return self.addtive(num)
  def isMatch(self, a, b, n):
    if len(a) > 1 and a[0] == '0': return False
    if len(b) > 1 and b[0] == '0': return False
    if a + b == n: return False
    t,i = a + b,0
    last,head = a, b
    print a,b
    while i < len(n):
      if n[i] != t[i]: return False
      i += 1
      if i < len(n) and i >= len(t):
        t += str(int(last) + int(head))
        tmp = head
        head = str(int(last) + int(head))
        last = tmp
    return True

      
  def addtive(self, n):
    if len(n) < 3: return False
    for i in range(1, len(n)):
      for j in range(i+1, len(n)):
          if self.isMatch(n[:i], n[i:j], n) == True:
            return True
    return False

s = Solution()
#print s.isMatch('1','1','112358')
#print s.isMatch('1','1','112')
print s.addtive('112358')
print s.addtive('112')
print s.addtive('1023')
