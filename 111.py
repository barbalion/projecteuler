from tools import *
import time
t = time.perf_counter()
tt = time.perf_counter()

def calc(n):
  minp = 10 ** (n-1)
  maxp = minp * 10
  cnt = 0

  M = [0] * 10
  N = [0] * 10
  S = [0] * 10
  def countDigitsIn(p):
    global t
    for nn in range(n):
      di = 10**(n-nn-1)
      dt = p // di
      p -= dt * di
      cnt[dt] += 1
    return cnt

  for p in primesN2M(minp, maxp, 100000000):
    global t
    if time.perf_counter() - t > 1:
      print(p, int(time.perf_counter() - tt), (time.perf_counter() - tt) / (p-minp)  * (maxp-minp))
      t = time.perf_counter()
    cnt = [0] * 10
    for (d, c) in zip(range(10), countDigitsIn(p)):
      if c > M[d]:
        M[d] = c
        N[d] = 0
        S[d] = 0
      if c == M[d]:
        N[d] += 1
        S[d] += p
  return list(zip(range(10), M, N, S))

n = 10
stat = calc(n)
print(n, stat)
print(sum([s for (d, m, n, s) in stat]))

print(time.perf_counter() - tt)
