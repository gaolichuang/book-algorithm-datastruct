# BackTracking I

回溯， 总是伴随这递归和剪枝。通过几个经典例子来体会下。 


##Question
##### 1. [leetcode][medium]Subsets 会有重复
> Given a set of distinct integers, nums, return all possible subsets.  

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
```
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```
问题分析
  - 这道题目的特点是可以重复
  - 使用最基础方式， 按照顺序， 第一个不要，或者要， 剩下的给递归处理
  - 注意跟下边题目对比
    - 按照长度分类， for i in range， 这样保证每次搞出来相同长度的，再来一次总的

```python
def solution(sets):
    subsets(sets, len(sets), 0, [])
def subsets(sets, n, idx, ret):
    '''
    经典的输入参数：
        sets: 集合本身
        n: 集合长度
        idx: 目前处理到哪里了
        ret: 输出集合
    '''
    if n <= idx: # 退出条件先写， 如果目前处理完了全部长度则输出
        print ret 
        return
    subsets(sets, n, idx + 1, ret) #第一个元素不放到集合中
    ret.append(sets[idx])  #第一个元素放到集合中
    subsets(sets, n, idx + 1, ret)
    ret.pop()  # 还原
```

##### 2. Subsets 只要指定长度的子集
For example,  nums = [1,2,3], target length = 2
```
If nums = [1,2,3], a solution is:
[
  [1,3],
  [2,3],
  [1,2],
]
```

问题分析
  - 这道题目的特点是可以重复
  - 只要指定长度的结果， 看代码

```python
def solution(sets, n):
      rets = []
      subsetsLength(sets, n, 0, [], rets)
      return rets
def subsetsLength(sets, n, idx, ret, rets):
    '''
        经典的输入参数：
        sets: 集合本身
        n: 指定需要的长度
        idx: 目前处理到哪里了
        ret: 一次指定有效结果
        rets： 整体结果集合
    '''
    if n == idx:
        retv = copy.deepcopy(map(lambda x : sets[x], ret))
        rets.append(retv)
        return
    for i in range(idx, len(sets)): #按照顺序， 要第i个； 或者loop后不要。
      ret.append(i)
      subsetsLength(sets, n, idx + 1, ret, rets)
      ret.pop()
```
##### 3. [leetcode][medium]Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
  - Elements in a subset must be in non-descending order.
  - The solution set must not contain duplicate subsets.
   
For example,
```
If nums = [1,2,2], a solution is:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

问题分析
   - 不能重复， 则需要先对输入序列排序， 然后保证前后不重复
   - 按照长度分类， for i in range， 这样保证每次搞出来相同长度的，再来一次总的
   - 见代码

```python
def solution(sets):
    rets = []
#按照长度得到所有的值
    for i in range(0, len(sets) + 1):
      subsetsWithDup(sets, i, 0, [], rets)
    return rets
#指定长度的一组集合
def subsetsWithDup(sets, n, idx, ret, rets):
    if n == idx:
        retv = copy.deepcopy(map(lambda x : sets[x], ret))
        if rets and rets[-1] == retv:
          return
        rets.append(retv)
        return
    for i in range(idx, len(sets)):
      if i in ret: # 单词中去掉重复
        continue
      if ret and ret[-1] > i:
        continue
      ret.append(i)
      subsetsWithDup(sets, n, idx + 1, ret, rets)
      ret.pop()
```
##### 4. [leetcode][medium]Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.  
For example, given n = 3, a solution set is:
```
"((()))", "(()())", "(())()", "()(())", "()()()"
```
问题分析
  - 两段，有两个变量在动
  - 参看代码
 
```python
def solution(n):
    dfs(n,n,[])
def dfs(left, right, ret):
    if left == 0 and right == 0: # 出口
      print ''.join(ret)
      return
    if left > 0 and left <= right:  # 处理左边括号， 保证左边比右边多
        ret.append('(')  #放入集合
        left = left - 1  # left加入 
        dfs(left, right, ret) # 递归， 
        left = left + 1 # 还原
        ret.pop()
    if right > 0: # 处理右边
        ret.append(')')
        right = right - 1
        dfs(left, right, ret)
        right = right + 1
        ret.pop()
```
---

**下边几个问题都是关于combination的**
##### 5. [leetcode][medium]Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.  
For example,
```
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```
问题分析
  - 获得指定长度的组合， 跟之前的题目2类似
```python
class Solution(object):
  def combine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    rets = []
    self.dfs(range(1, n + 1), 0, k, [], rets)
    return rets
  def dfs(self, n, idx, k, ret, rets):
    if idx == k:
      rets.append(copy.deepcopy(ret))
      print ret
      return
    #下边这个可以避免重复，递归和循环一起会错乱， so， start的位置需要根据ret来决定
    # 保证每次都是从当前位置的后边拿
    start = ret[-1] if ret else 1 
    for i in range(start, len(n) + 1):
      if i in ret:
        continue
      ret.append(i)
      self.dfs(n, idx + 1, k, ret, rets)
      ret.pop()
```
##### 5. [leetcode][medium]Combination Sum
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
> All numbers (including target) will be positive integers.  
> Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).   
> The solution set must not contain duplicate combinations.  
```
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
```

问题分析
   -  可以重复拿，加和是指定数即可

```python
  def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    rets = []
    self.dfs(candidates, target, [], rets)
    return rets
  def dfs(self, can, target,ans,rets):
    if target == 0:
      import copy
      rets.append(copy.deepcopy(ans))
      return
    for c in can: # 因为可以重复， 则每次都重新开始
      if c > target:
        continue
      if ans and c < ans[-1]:
        continue
      ans.append(c)
      self.dfs(can, target - c, ans, rets)
      ans.pop()
```

##### 6. [leetcode][medium] Combination Sum II
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
> All numbers (including target) will be positive integers.
> Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
> The solution set must not contain duplicate combinations.
```
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
```
问题分析
  - 关键在不能重复
```python
  def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    rets = []
    self.dfs(sorted(candidates), target, [], rets) # 先要排序
    return rets

  def dfs(self, can, target, ans, rets):
    '''
      ans is index at can
    '''
    if target == 0:
      import copy
      rets.append([can[k] for k in ans])
      return
    last = None #last保证拿的元素不和之前相同，这依赖于排序
    start = ans[-1] + 1 if ans else 0 # 起始位置保证会回头拿
    for i in range(start, len(can)):
      c = can[i]
      if last == c:
        continue
      if c > target:
        continue
      last = c
      ans.append(i)
      self.dfs(can, target - c, ans, rets)
      ans.pop()
```


##### 7. [leetcode][medium] Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.
```
Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]
```
```
Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]
```
问题分析
   - 不重复
```python
  def combinationSum3(self, k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    rets = []
    self.dfs(range(1,n+1), n, k, [], rets)
    return rets

  def dfs(self, can, n, k, ans, rets):
    '''
      ans is index at can
    '''
    if len(ans) > k:  # 剪枝
      return
    if len(ans) == k and n == 0:
      import copy
      rets.append(copy.deepcopy(ans))
      return
    start = ans[-1] + 1 if ans else 1 # 别重复
    for i in range(start, len(can)):
      ans.append(i)
      self.dfs(can, n - i,k, ans, rets)
      ans.pop()
```

##### 8.[leetcode][medium] Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
```
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
问题分析
  - 遍历，穷举， 这种问题更容易解决

```python
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
    phonemap = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    rets = []
    self.dfs(digits,0,'',rets, phonemap)
    return rets
  def dfs(self, num, idx, ans, rets, phone):
    if idx == len(num):
      rets.append(ans)
      return
    for a in phone[int(num[idx])]:
      self.dfs(num,idx+1,ans+a,rets, phone)
```