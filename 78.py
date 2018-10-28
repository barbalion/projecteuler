from tools import *
import math

cac = []

def K(n, l):
  res = 0
  if n <= l:
    res += 1
    l = n
  # prep cache
  for i in range(n-len(cac)):
    cac.append([])
  for i in range(l-len(cac[n-1])):
    cac[n-1].append(0)
  # check in the cache
  if cac[n-1][l-1] > 0:
    return cac[n-1][l-1]
  # calc recursively
  for i in range(1, min(n, l + 1)):
    res += K(n-i, i)

  #put the result into the cache and return
  cac[n-1][l-1] = res
  return res
    

def A(n, k):
  if k <= 1:
    return k
  elif k == 2:
    if n % 2 == 0:
      return 1
    else:
      return -1
  s, r, m = 0, 2, n % k
  for l in range(2* k):
    if m == 0:
      l1 = 1 - (l % 2)*2
      s += l*math.cos(math.pi*(6*l+1)/(6*k))
    m = m + r
    if m >=k:
      m -= k
    r += 3
    if r >= k:
      r -= k
  return math.sqrt(k/3)*s

def A2(n, k):
  fac = factor(k)
  j = len(fac)
  s = 1
  for i in range(j):
    if i < j - 1:
      k1 = fac[i][0] ** fac[i][1]
      k2 = k // k1
      n1, n2 = 0, 0#...
      s *= A2(n1, k1)
      k, n = k2, n2
    else:
      s *= A2(n, k)
  return s

#def K2(n):
#  N = 100 #?
#  C = Pi/6*math.sqrt(24 * n - 1)
#  u = math.exp(C)
#  s1, s2 = 0, 0
#  for k in range(1, N+1):
    

#n = 1000
#print(A(5, 10)) 

for n in range(1, 1001):
  print(n, K(n, n)) 

print(cac)