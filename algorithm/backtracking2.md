# BackTracking II

主要是实际的题目供理解。   
0/1背包，排列组合，   
http://fuliang.iteye.com/blog/164686  
http://blog.csdn.net/m6830098/article/details/17596529  


##Question
##### 1. [leetcode][medium]N-Queens
N-Queens My Submissions Question
The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
    There exist two distinct solutions to the 4-queens puzzle:

    [
    [".Q..",  // Solution 1
    "...Q",
    "Q...",
    "..Q."],

    ["..Q.",  // Solution 2
    "Q...",
    "...Q",
    ".Q.."]
    ]

##### 2.[leetcode][medium]Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",  
Return
```
  [
    ["aa","b"],
    ["a","a","b"]
  ]
```
问题分析：
  - 从头开始找回文， 找到后， 递归继续
```python
  def p(self, s, ret, rets):
    import copy
    if len(s) == 0:
      rets.append(copy.deepcopy(ret))
      return
    for i in range(1, len(s)+1):
      if not self.isp(s[:i]):
        continue
      ret.append(s[:i])
      self.p(s[i:],ret,rets)
      ret.pop()
```

##### 3.[leetcode][medium]Permutations
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

```python
  def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    rets = []
    self.dfs(nums, 0, len(nums), rets)
    return rets
  def dfs(self, num, idx, n, rets):
    if idx >= n:
      rets.append(copy.deepcopy(num))
      return
    for i in range(idx, n):
      num[idx],num[i] = num[i],num[idx]
      self.dfs(num, idx + 1, n, rets)
      num[idx],num[i] = num[i],num[idx]
```

##### 4.[leetcode][medium]Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

```python
  def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    rets = []
    self.dfs(sorted(nums), 0, len(nums), rets)
    return rets

  def dfs(self, num, idx, n, rets):
    if idx >= n:
      rets.append(copy.deepcopy(num))
      return
    pre = []
    for i in range(idx, n):
      if num[i] in pre: continue   # 去重复
      pre.append(num[i])
      num[idx],num[i] = num[i],num[idx]
      self.dfs(num, idx + 1, n, rets)
      num[idx],num[i] = num[i],num[idx]
```
##### 5. [leetcode][medium]Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

###### 6. split sum
加法因式分解
```python
def solution(n):
    split_sum_dfs(n, [])

def split_sum_dfs(n, ret):
  if n <= 0 and len(ret) > 1:
    print ret
    return
  # not duplicate
  start = ret[-1] if ret else 1
  for i in range (start, n+1):
      ret.append(i)
      split_sum_dfs(n - i, ret)
      ret.pop()
```

##### 7. [leetcode][medium]word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
```
Given board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
```
问题分析
   - 图， 遍历， 穷举