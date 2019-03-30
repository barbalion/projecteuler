from tools import *
from functools import reduce
P = 25000000
maxA = int(0.3*P) 

memDivs = [None]*(maxA + 2)
def divs(a):
  a2 = a
  if memDivs[a2]:
    return memDivs[a2]
  res = [1]

  for p in primesN2M(2, int(a **.5)):
    cnt = 0
    while a % p == 0:
      a //= p
      cnt += 1
    if cnt > 0:
      res = [d * p**n for n in range(cnt+1) for d in res]
    if a == 1:
      break
  if a > 1:
    res += [d * a  for d in res]
  memDivs[a2] = res
  return res    

t = (P - 1) // 2 # {1, n, n} is allways a solution, just skip it

cachePrimes(maxA)
storeTimes = 1000
resetTime()
mm=1+2**.5
for a in range(2, maxA + 1):
  a21 = a**2-1
  d1s = divs((a-1)//(1+a%2*(((a-1)//2)%2)))
  d2s = divs((a+1)//(1+a%2*(((a+1)//2)%2)))
  for d1 in d1s:
    for d2 in d2s:
      p = d1*d2
      q = a21 // p
      if (p >= int(a * mm)) and (p <= P - a) and (p+q)&1 == 0:
        t +=1
  
  if a % 10000 == 0:
    elapsed((a, 1, maxA))
  if a % 200000 == 0: # reset cache to free some memory
    memDivs = [None]*(maxA + 2)

print(t)

elapsed()
