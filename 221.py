from tools import *
from collections import deque

def check(a, p, q, r):
  d = p*q+q*r+r*p
  pd = p*q*r
  if a == pd and d!=0 and a==pd//d:
    print(f'{a}: {p},{-q},{-r}')
    return 1
  else:
    return 0

def find(a):
  ds = divs(a)
  ds.sort()
  for p in ds:
    for q in ds:
      for r in ds:
        if check(a, p, -q, -r):
          return 1
  return 0

N = 20

cnt = 0
a = 1
while cnt < N:
  a += 1
  cnt += find(a)
