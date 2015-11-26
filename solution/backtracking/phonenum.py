'''
Letter Combinations of a Phone Number My Submissions Question
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

'''
class Solution(object):
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phonemap = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    rets = []
    self.dfs(digits,0,'',rets, phonemap)
    return rets
  def dfs(self, num, idx, ans, rets, phone):
    if idx == len(num):
      print ans
      rets.append(ans)
      return
    for a in phone[int(num[idx])]:
      self.dfs(num,idx+1,ans+a,rets, phone)
s = Solution()
#print s.letterCombinations('23')
print s.letterCombinations('2335')
