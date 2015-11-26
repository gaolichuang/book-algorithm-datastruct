def solution(A, X):
    N = len(A)
    if N == 0:
      return -1
    l = 0
    r = N - 1
    while l < r:
      m = (l + r) // 2
      if A[m] >= X:
        r = m if A[m] == X else m - 1
      else:
        l = m if A[m] == X else m + 1
    if A[l] == X:
      return l
    return -1



print solution([1,2,3,4,5],3)
print "XXX"
print solution([1,2,3,4,5],0)
print solution([1,2,3,4,5],1)
print solution([1,2,3,4,5],2)
print solution([1,2,3,4,5],4)
print solution([1,2,3,4,5],5)
print solution([1,2,3,4],4)
print solution([1,2],4)
print solution([1],1)
print solution([],1)
print solution(None,1)
