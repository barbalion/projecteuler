from tools import *
from heapq import *

N = 150000

def cnt(u):
  res = [u[0][0]]
  while len(res) < N*2:
    _, p, q, r = heappop(u)
    for p, q, r in [(q, -p + 2*q, 2*q + r), (r, -p + 2*r, 2*r + q)]:
      A = p*q*r
      heappush(u, (A, p, q, r))
      res.append(A)
  return res

res = cnt([(6, 1, 2, 3)])
res.sort()
print(res[N-1])

elapsed()
