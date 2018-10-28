s = 20
cache = [[0 for _ in range(s+1)] for _ in range(s+1)]

def N(x, y):
  c = cache[x][y]
  if c > 0:
    return c
  if x == 0 or y == 0:
    res = 1
  else:
    res = N(x-1, y) + N(x, y-1)
  cache[x][y] = res
  return res

print(N(s, s))
