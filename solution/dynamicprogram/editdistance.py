'''
Edit Distance My Submissions Question
Total Accepted: 46507 Total Submissions: 171567 Difficulty: Hard
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

    You have the following 3 operations permitted on a word:

    a) Insert a character
    b) Delete a character
    c) Replace a character
'''
'''
edit[i][j] = min(edit[i-1][j]+1
                 edit[i][j-1] + 1
                 edit[i-1][j-1] + f(i,j))
if word1[i] == word2[j] f(i,j) = 0 else 1
'''
class Solution(object):
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    s,t = word1,word2
    lens,lent = len(s),len(t)
    d = [[0]*(lens + 1) for k in range(lent+1)]
    for i in range(lens+1):
      d[0][i] = i
    for i in range(lent+1):
      d[i][0] = i
    for i in range(1,lent+1):
      for j in range(1,lens+1):
        tl = d[i-1][j-1]
        tl = tl + 1 if t[i-1] != s[j-1] else tl
        if tl < d[i-1][j] + 1:
          if tl < d[i][j-1] + 1:
            d[i][j] = tl
          else:
            d[i][j] = d[i][j-1] + 1
        else:
          if d[i-1][j] < d[i][j-1]:
            d[i][j] = d[i-1][j]+1
          else:
            d[i][j] = d[i][j-1] + 1
    for i in d:
        print i
    return d[lent][lens]
s = Solution()
#s.minDistance('abc','aaaa')
#s.minDistance('','a')
#s.minDistance('a','a')
s.minDistance('a','ab')


