from tools import *

def cnt(q, P):
  res = 0
  while q:
    a, b, c = q.pop()
    while a + b + c <= P:
      res += 1
      if 5*(a + b) + 7*c <= P:
        q.append((2*a + b + 2*c,a + 2*b + 2*c,2*a + 2*b + 3*c))
      if a != b and 5*(a - b) + 7*c <= P:
        q.append((a - 2*b + 2*c,2*a - b + 2*c,2*a - 2*b + 3*c))
      a, b, c = -2*a + b + 2*c,-a + 2*b + 2*c,-2*a + 2*b + 3*c
  return res

print(cnt([(2, 2, 3)], 75000000))

elapsed()
