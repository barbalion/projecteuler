from tools import *
#from heapq import *
from collections import deque

N = 10**4
Ns = int(N ** .5)

def check(c):
  for p, n in factorC(c):
    if n >= 2:
      return False
  return True

res = 0
tot = 0
for a in range(1, Ns+1):
  for b in range(0, int((N - a**2)**.5)+1):
    c = a + 1j*b
    tot += 1
    if check(c):
      res += 1

print(tot, res)
elapsed()