from tools import *

N = 10**9

cachePrimes(int(N**.5))

pp=0
for p in primesN2M(2, N):
  if p-pp > 200:
    print(p, pp-p)
  pp = p

