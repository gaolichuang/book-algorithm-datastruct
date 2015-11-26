
import copy

def solution(sets):
#    subsets(sets, len(sets), 0, [])
    rets = []
    for i in range(0, len(sets) + 1):
      rets = []
      subsetsWithDup(sets, i, 0, [], rets)
      print rets
    return rets
def subsetsWithDup(sets, n, idx, ret, rets):
    if n == idx:
        retv = copy.deepcopy(map(lambda x : sets[x], ret))
        if rets and rets[-1] == retv:
          return
        rets.append(retv)
        return
    for i in range(idx, len(sets)):
      if i in ret:
        continue
      if ret and ret[-1] > i:
        continue
      ret.append(i)
      subsetsWithDup(sets, n, idx + 1, ret, rets)
      ret.pop()

def subsets(sets, n, idx, ret):
    '''
        n: lengths of sets
        idx: current depth
    '''
    if n <= idx:
        print ret
        return
    subsets(sets, n, idx + 1, ret)
    ret.append(sets[idx])
    subsets(sets, n, idx + 1, ret)
    ret.pop()

print solution([2,2,2,2,3,3])
#solution([1])
