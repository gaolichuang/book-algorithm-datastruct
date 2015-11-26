# Depth/Breath-First-Search

BFS 能做的 DFS 也能做， 反过来DFS能做的BFS也可以做  
找最短、最少的遍历问题， 就得想到BFS,因为这种情况BFS 收敛快  

## Question
##### 1.[leetcode][hard]Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).
```
Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
```

问题分析
  -  本题可以用DFS也可以BFS，但由于本题求的是最小次数而非第一个匹配的结果，因此BFS比较合适。
  - 如果s不符合要求，对s的第i位进行移除，i∈[0,n)，得到新字符串t1,t2,t3…判断t[1…n]是否符合要求，如果符合要求则依次加入结果集中；否则将t[0…n)加入队列中即可。
  - 遍历过程中由于可能存在t已经判断过，可使用字典来做剪枝。

##### 2.[leetcode][hard]Word Ladder II
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

 > Only one letter can be changed at a time  
 > Each intermediate word must exist in the word list  
For example,
```
Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
```
Note:  
> All words have the same length.  
> All words contain only lowercase alphabetic characters.

问题分析：
   - 单词之间可以通过转换得到， 通过BFS进行搜索得到最快的一个结果
   - 1.需要有个去重的东西
   - 2.bfs，找到最短的

##### 3.[leetcode][medium]Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
```
Example 1:

11110
11010
11000
00000
Answer: 1
```
```
Example 2:

11000
11000
00100
00011
Answer: 3
```

问题分析
  -  有少个联通图
```
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    g = []
    count = 0
    for i in grid: g.append(list(i))
    for i in range(len(g)):
      for j in range(len(g[0])):
        if g[i][j] == '1':
          self.dfs(g,i,j,len(g),len(g[0]))
          count += 1
    return count

  def dfs(self, g, i, j, lr, lw):
    if i < 0 or i >= lr or j < 0 or j >= lw or g[i][j] != '1': return
    g[i][j] = '0'
    self.dfs(g,i+1,j,lr,lw)
    self.dfs(g,i,j-1,lr,lw)
    self.dfs(g,i-1,j,lr,lw)
    self.dfs(g,i,j+1,lr,lw)


```
##### 4.[leetcode][hard]Expression Add Operators
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
```
Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
```

http://segmentfault.com/a/1190000003797204   
乘号之前是加号或减号，例如2+3*4，我们在2那里算出来的结果，到3的时候会加上3，计算结果变为5。在到4的时候，因为4之前我们选择的是乘号，这里3就应该和4相乘，而不是和2相加，所以在计算结果时，要将5先减去刚才加的3得到2，然后再加上3乘以4，得到2+12=14，这样14就是到4为止时的计算结果。
另外一种情况是乘号之前也是乘号，如果2+3*4*5，这里我们到4为止计算的结果是14了，然后我们到5的时候又是乘号，这时候我们要把刚才加的3*4给去掉，然后再加上3*4*5，也就是14-3*4+3*4*5=62。这样5的计算结果就是62。
因为要解决上述几种情况，我们需要这么几个变量，一个是记录上次的计算结果currRes，一个是记录上次被加或者被减的数prevNum，一个是当前准备处理的数currNum。当下一轮搜索是加减法时，prevNum就是简单换成currNum，当下一轮搜索是乘法时，prevNum是prevNum乘以currNum。


##### 5.[leetcode][hard]Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,
```
       1
      / \
     2   3
Return 6.
```
```python
  def dfs(self, root):
    if root == None: return 0
    v = root.val
    rmax,lmax = -sys.maxint,-sys.maxint
    if root.left is not None:
      lmax = self.dfs(root.left)
      if lmax > 0:
        v += lmax
    if root.right is not None:
      rmax = self.dfs(root.right)
      if rmax > 0:
        v += rmax
    if v > self.vmax:
      self.vmax = v
    return self.maxs(root.val, self.maxs(rmax+root.val,lmax+root.val))
```

## TODO
1. Code
2. Other Questions