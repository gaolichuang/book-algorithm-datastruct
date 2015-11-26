'''
Add and Search Word - Data structure design My Submissions Question

Design a data structure that supports the following two operations:

void addWord(word)
    bool search(word)
    search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

    For example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true
    Note:
    You may assume that all words are consist of lowercase letters a-z.
'''
class TrieNode(object):
  def __init__(self):
    self.isword = False
    # key is letter, value is TrieNode reference
    self.children = {}
class Trie(object):
  def __init__(self):
    self.root = TrieNode()
  def add(self, w):
    current = self.root
    for l in w:
      if l not in current.children.keys():
        current.children[l] = TrieNode()
      current = current.children[l]
    current.isword = True

  def delete(self, w):
    path = []
    cur = self.root
    path.append(cur)
    for l in w:
      if l not in cur.children.keys():
        return False
      cur = cur.children[l]
      path.append(cur)
    if not cur.isword:
        return False
    path[-1].isword = False
    for i in reversed(range(0, len(path))):
      path[i-1].children.pop(w[i-1])
      if len(path[i-1].children.keys()) != 0:
        break
 
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

class WordDictionary(object):
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.trie = Trie()

  def addWord(self, word):
    """
    Adds a word into the data structure.
    :type word: str
    :rtype: void
    """
    self.trie.add(word)

  def search(self, word):
    """
    Returns if the word is in the data structure. A word could
    contain the dot character '.' to represent any one letter.
    :type word: str
    :rtype: bool
    """
    return self.trie.searchpattern(word)


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
print wordDictionary.search("w...")
