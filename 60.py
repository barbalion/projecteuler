from tools import *
import sys

chkmem = [];

def chk(b, a):
  if a >= len(chkmem):
    for i in range(len(chkmem), a+1):
      chkmem.append([])
  if b >= len(chkmem[a]):
    for i in range(len(chkmem[a]), b+1):
      chkmem[a].append(0)
  if chkmem[a][b] == 0:
    chkmem[a][b] = 1 if isPrime(int(str(primeN(a))+str(primeN(b)))) and isPrime(int(str(primeN(b))+str(primeN(a)))) else -1
  return chkmem[a][b] == 1

def chkAll(lst):
  for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
      if not chk(lst[i], lst[j]):
        return False
  return True

def chkNew(lst, n):
  for i in range(len(lst)):
    if not chk(lst[i], n):
      return False
  return True

m = 2
minS = 0
found = [[]]
for n in range(2000):
  for i in range(len(found)):
    test = found[i] + [n]
    if chkNew(found[i], n):
      found += [test]
      if len(test) > m:
        m = len(test)
        minS = 0
      if len(test) == m:
        ps = [primeN(i) for i in test]
        s = sum(ps)
        if s < minS or minS == 0:
          minS = s
          print(n, m, ps, s)
          if m == 5:
            sys.exit(0)
  print(n, end='\r')
