from tools import *
from functools import reduce

def perm(p, n, positions): # all permutations of N-digit number containing all P digits
  return [p] if len(p) == n else sum([perm(p[0:i]+[d]+p[i:], n, range(i+1, len(p) + 2)) for d in range(10) for i in positions], [])

def primesWithMDs(n, m, d): # all prime N-digit numbers with M 'D's.
  return [p for p in [reduce(lambda a, b: a * 10 + b, c) for c in perm([d] * m, n, range(m + 1)) if c[0] > 0] if isPrime(p)]

def calc(n):
  S = [0] * 10
  for d in range(10):
    for m in range(n-1, 0, -1):
      for p in primesWithMDs(n, m, d):
        S[d] += p
      if S[d] > 0:
        break 
  return S

print(sum(calc(10)))
