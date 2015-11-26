'''
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

    Given:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    Return
      [
          ["hit","hot","dot","dog","cog"],
          ["hit","hot","lot","log","cog"]
      ]
'''
import copy
class Solution(object):
  def __init__(self):
    self.rets = []
    self.nstep = {}
    self.fail = []
  def findLadders(self, beginWord, endWord, wordlist):
    """
    :type beginWord: str
    :type endWord: str
    :type wordlist: Set[str]
    :rtype: List[List[int]]
    """
    self.buildstep(beginWord,endWord,wordlist)
    print self.nstep
    self.dfs(beginWord, endWord, wordlist, [beginWord])
    return self.rets
  def buildstep(self, start, end, wordlist):
    allword = set([start,end] + list(wordlist))
    for word in allword:
      for i in range(len(word)):
        pre = word[:i]
        sub = word[i+1:]
        for j in 'abcdefghijklmnopqrstuvwxyz':
          if word[i] != j:
            if pre + j + sub in allword:
              try:
                self.nstep[word].append(pre + j +sub)
              except:
                self.nstep[word] = [pre + j +sub]
  def worddis(self, worda, wordb):
    for i in range(len(worda)):
      if worda[i] != wordb[i]:
        return i
    return None
  def dfs(self, begin, end, wordlist, ret):
    if begin == end:
      if self.rets:
        if len(self.rets[0]) > len(ret):
          self.rets = [copy.deepcopy(ret)]
        elif len(self.rets[0]) == len(ret):
          self.rets.append(copy.deepcopy(ret))
      else:
        self.rets = [copy.deepcopy(ret)]
      return
    if len(ret) >= len(wordlist):
      print ret
      return
    finish = True
    for w in self.nstep[begin]:
      if w in ret:
        continue
      if w in set(self.fail):
        continue
      lastidx = -1
      if len(ret) > 1:
        lastidx = self.worddis(ret[-2], begin)
      idx = self.worddis(w, begin)
      if lastidx == idx:
        continue
      finish = False
      ret.append(w)
      print ret,self.fail
      self.dfs(w, end, wordlist, ret)
      ret.pop()
    if finish:
      self.fail.append(begin)

s = Solution()
#print s.findLadders('a', 'c',['a','b','c'])
#print s.findLadders("qa",
#      "sq",
#      ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])
print s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log"])
