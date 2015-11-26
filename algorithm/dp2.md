# Dynamic Program II

二维动态规划，DP的过程就是从小算到大，记录计算历史，避免重复计算

##Question
##### 1. [leetcode][Medium]Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


问题分析：
   -  二维动态规划，一般d[][]都会多一个行列做初始化
   -  只能从上边或左边过来
```python
  def dp(self, grid):
    '''
      dp[i][j] = max(dp[i-1][j],d[[i][j-1]) + grid[i][j]
    '''
    lenm,lenn = len(grid),len(grid[0])
    d = [[0]*(lenn+1) for k in range(lenm+1)]
    import sys
    for i in range(lenn+1): d[0][i] = sys.maxint
    for i in range(lenm+1): d[i][0] = sys.maxint
    for i in range(1,lenm+1):
      for j in range(1,lenn+1):
        if d[i][j-1] ==  sys.maxint and d[i-1][j] ==sys.maxint:
          d[i][j] = grid[i-1][j-1]
          continue
        if d[i-1][j] > d[i][j-1]:
          d[i][j] = grid[i-1][j-1] + d[i][j-1]
        else:
          d[i][j] = grid[i-1][j-1] + d[i-1][j]
    return d[lenm][lenn]
```

##### 2.[leetcode][medium]Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
```

问题分析：
  - 正方形， 以右下顶点计算， 则正方形大小跟上，左上，左有关
  - 计算关系
```
        if matrix[i-1][j-1] == '0':
          d[i][j] = 0
          continue
        d[i][j] = self.mins(self.mins(d[i-1][j-1],
                                        d[i-1][j]),
                                        d[i][j-1])+1
        gmax = d[i][j] if d[i][j] > gmax else gmax
```

##### 3.[leetcode][medium]Distinct Subsequences
Given a string S and a string T, count the number of distinct subsequences of T in S. Only delete char from S
Sample:S = "rabbbit", T = "rabbit" Return 3

问题分析：
  - DP问题难点在于能够理解算法思路

```
if s[i] == t[j]:
    d[i][j] = d[i-1][j-1] + d[i-1][j] # not del or  del
else
    d[i][j]=d[i-1][j] # del
```

##### 4.[leetcode][medium]Interleaving String
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
```
For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
```
问题分析：
  - 找状态转换方程
  - isInterleaving(s1,len1,s2,len2,s3,len3)
  = (s3.lastChar == s1.lastChar) && isInterleaving(s1,len1 - 1,s2,len2,s3,len3 - 1)
    ||(s3.lastChar == s2.lastChar) && isInterleaving(s1,len1,s2,len2 - 1,s3,len3 - 1)



##### 5.[leetcode][hard]Edit Distance
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)  
You have the following 3 operations permitted on a word:  
>a) Insert a character  
>b) Delete a character  
>c) Replace a character

问题分析：
  - 找状态转换方程
```
    a) Insert a character
    b) Delete a character
    c) Replace a character
edit[i][j] = min(edit[i-1][j]+1
                 edit[i][j-1] + 1
                 edit[i-1][j-1] + f(i,j))
if word1[i] == word2[j] f(i,j) = 0 else 1
```

##### 6.[leetcode][Medium]Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,  
Given [10, 9, 2, 5, 3, 7, 101, 18],  
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.  

Your algorithm should run in O(n2) complexity.  

Follow up: Could you improve it to O(n log n) time complexity?

问题分析：
   - 这个问题和之前的有些不同， A[i]的长度要跟A[0]--A[i-1]都做比较
   - Long[i] = max(A[0] + A[i]? .... A[i-1] + A[i])
   

##### 7.[leetcode][Medium]Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4

问题分析：
   - DP需要将问题分析到细节，并能推广到全部
   - A[i]的计算， 如果A[i]为')'，并且去掉A[i-1]组成的有效长度后之前的是'('，则A[i] = A[i-1]+2; 并检查下，是否能跟这之前的合并在一起

```
  def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s: return 0
    l = len(s)
    d = [0]*l
    maxs = 0
    for i in range(1,l):
      if s[i] == ')' and i-d[i-1]-1 >=0 and s[i-d[i-1]-1] == '(':
        d[i] = 2 + d[i-1]
        if i - d[i-1]-2>0 and d[i-d[i-1]-2] != 0:
            d[i]+=d[i-d[i-1]-2]
      maxs = d[i] if d[i] > maxs else maxs
    return maxs
```

##### 7.[leetcode][Medium]Palindrome Partitioning II
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",  
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

问题分析
  - 这道题目跟最长递增子序列类似  for i  for j (0,i) min
```
    for i in range(1,ls+1):
      mins = ls
      for j in range(0,i):
        if s[i-1] != s[j]: continue
        if self.ispal(s,j,i-1):
          mins = p[j]+1 if mins > p[j]+1 else mins
```
##### 8. [leetcode][medium]Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

问题分析
  - 有的时候，递推关系未必是相邻的元素
 


##### 9. [leetcode][hard]Regular Expression Matching
Implement regular expression matching with support for '.' and '*'.
```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
```
问题分析
  - 二维， p[j]是*，则path[i][j]跟 path[i-2][j] or path[i-1][j]有关
  - 如果之前 有 .， 则还有跟path[i-1][j-1] or path[i][j-1] 有关

##### 9. [leetcode][hard]Wildcard Matching
Implement wildcard pattern matching with support for '?' and '*'.
```
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
```
问题分析
   - 遇到？或相等， 怎跟左上同path[i][j] = path[i-1][j-1]
   - 如果是*, 可以选择匹配 不匹配
```python
  def dp(self, s, p):
    path = [[False]*(len(s) + 1) for x in range(len(p) + 1)]
    path[0][0] = True
    for i in range(1, len(p) + 1):
      for j in range(1, len(s) + 1):
        if p[i-1] == '?' or p[i-1] == s[j-1]:
          path[i][j] = path[i-1][j-1]
        elif p[i-1] == '*':
          path[i][j] = path[i-1][j] or path[i][j-1]
    return path[len(p)][len(s)]
```

##### 10. [leetcode][hard]Maximal Rectangle
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

问题分析
  - hash table ， stack， dp

##### 10. [leetcode][hard] Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
```
For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

##### 11. [leetcode][hard] Unique Binary Search Trees II
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
```
For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```
##### 12.[leetcode][hard]Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

问题分析
  - 我们定义local[i][j]为在到达第i天时最多可进行j次交易并且最后一次交易在最后一天卖出的最大利润，此为局部最优。
  - 然后我们定义global[i][j]为在到达第i天时最多可进行j次交易的最大利润，此为全局最优。
  - 它们的递推式为：
local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)  

global[i][j] = max(local[i][j], global[i - 1][j])，  
http://blog.csdn.net/ljiabin/article/details/44900389  
http://www.cnblogs.com/grandyang/p/4295761.html
