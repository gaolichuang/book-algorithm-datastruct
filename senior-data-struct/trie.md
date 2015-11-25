# Trie Tree

字典树，前缀树  
以下单词构建的trie树结构，  who，how, why, what,wo, we, hi
```
       root
      /     \
     w       h
   / | \    / \
  h  o  e  o   i
 /\        /
o  y      w
```
特点：
> 根节点不包含字符  
> 公共前缀保存一份  
> 有限字符集
用途：
> 词频统计
> 前缀匹配

```
class TrieNode:
  # Initialize your data structure here.
  def __init__(self):
    self.childs = dict()
    self.isWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
    node = self.root
    for letter in word:
      child = node.childs.get(letter)
      if child is None:
        child = TrieNode()
        node.childs[letter] = child
      node = child
    node.isWord = True

  def delete(self, word):
    node = self.root
    queue = []
    for letter in word:
      queue.append((letter, node))
      child = node.childs.get(letter)
      if child is None:
        return False
      node = child
    if not node.isWord:
      return False
    if len(node.childs):
      node.isWord = False
    else:
      for letter, node in reversed(queue):
        del node.childs[letter]
        if len(node.childs) or node.isWord:
          break
    return True
  def search(self, w):
    cur = self.root
    for l in w:
      if l not in cur.children.keys():
        return False
      cur = cur.children[l]
    return cur.isword
  def searchpattern(self, w):
    return self.dfs(w, self.root)
  def dfs(self, w, root):
    if len(w) == 0:
      return root.isword
    if w[0] == '.':
      for ch in root.children.keys():
        if True == self.dfs(w[1:], root.children[ch]):
          return True
    elif w[0] in root.children.keys():
      return self.dfs(w[1:], root.children[w[0]])
    return False
```


## Question
##### 1. [leetcode][medium]Add and Search Word - Data structure design
Design a data structure that supports the following two operations:  
```
void addWord(word)
bool search(word)
```
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.  
For example:
```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```
Note:
You may assume that a-z
