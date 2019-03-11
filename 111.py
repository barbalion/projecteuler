from tools import *
from functools import reduce

def perm(p, n, nn):
  if len(p) == n:
    return [p]
  return sum([perm(p[0:i]+[d]+p[i:], n, range(i+1, len(p) + 2)) for d in range(10) for i in nn], [])

def primesWithMDs(n, m, d):
  for c in perm([d] * m, n, range(m + 1)):
    p = reduce(lambda a, b: a * 10 + b, c)
    if c[0] > 0 and isPrime(p):
      yield p

def calc(n):
  minp = 10 ** (n-1)
  maxp = minp * 10
  cnt = 0

  M = [0] * 10
  N = [0] * 10
  S = [0] * 10
  
  for d in range(10):
    for m in range(n-1, 0, -1):
      for p in primesWithMDs(n, m, d):
        M[d] = m
        N[d] += 1
        S[d] += p
      if M[d] > 0:
        break 
  return list(zip(range(10), M, N, S))

n = 10
stat = calc(n)
#print(n, stat)
print(sum([s for (d, m, n, s) in stat]))
