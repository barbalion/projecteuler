import operator, functools
import math, pdb
import sys
from decimal import *

rm = 0
rn = 0
srm =0

def powmod(x, n, m):
  p = 1
  for i in range(2, n+1):
    p = (p* x) % m
  return p

print(powmod(23, 3, 13))

for a in range(3, 1001):
  rm = 0
  for n in range(2*a, 4*a):
    r = (powmod(a-1, n, a*a) + powmod(a+1, n, a*a)) % (a*a)
    if r > rm:
      rm = r
      rn = n
  srm += rm
  print(a, rn, rm, srm)
      