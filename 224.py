from tools import *

def cnt(q, P):
  res = 0
  while q:
    a, b, c = q.pop(-1)
    while a + b + c <= P:
      res += 1
      q += [
        (2*a + b + 2*c,a + 2*b + 2*c,2*a + 2*b + 3*c),
      ] + ([
        (a - 2*b + 2*c,2*a - b + 2*c,2*a - 2*b + 3*c)
      ] if a != b else [])
      a, b, c = -2*a + b + 2*c,-a + 2*b + 2*c,-2*a + 2*b + 3*c
  return res

print(cnt([(2, 2, 3)], 75000000))

elapsed()
