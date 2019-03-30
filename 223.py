from tools import *
from functools import reduce
P = 25000000

def divs(f, m):
  if not f:
    return [1] if m > 0 else []
  p, n = f[0]
  res = divs(f[1:], m)
  for r in res[:]:
    for i in range(1, n+1):
      s = p ** i * r
      if s <= m:
        res += [s]
  return res

t = (P - 1) // 2 + 1 # {1, n, n} is allways a solution, just skip it

maxA = int(0.3*P) # approx maxA when minN==maxN
cachePrimes(maxA)
storeTimes = 1000
resetTime()
for a in range(2, maxA + 1):
  maxN = int(a*0.414213562373) # approx maxN when b > a
  minN = (a*a-1)//(P-a) # when a + b + c > P
  f = factor((a**2-1)//(a%2+1))
  for n in divs(f, maxN):
    if n <= minN or (a+n)%2==0:
      continue
    t += 1
  
  if a % 10000 == 0:
    elapsed((a, 1, maxA))

print(t)

elapsed()
