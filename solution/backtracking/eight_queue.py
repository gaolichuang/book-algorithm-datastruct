def solution(n):
  dfs([], n)

def dfs(ret,n):
  if len(ret) >= n:
    print ret
    return
  for i in range(1,1+n):
    if i in ret:
      continue
    ret.append(i)
    dfs(ret,n)
    ret.pop()

solution(5)
