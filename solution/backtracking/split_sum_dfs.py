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

solution(5)
solution(10)
