from tools import *
from functools import reduce
P = 750
maxA = int(0.3*P) # approx maxA when minN==maxN

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
      #return [d * p**n for d in divs(a) for n in range(cnt+1)]
    if a == 1:
      break
  if a > 1:
    res += [d * a  for d in res]
  memDivs[a2] = res
  return res    

#print(list(divs(21)))
#exit()

def check(a, b, c):
  if a > b:
    a, b = b, a
  if a*a + b*b == c*c - 1 and a+b+c <= P:
    print(f'{a},{b},{c}: {a*a}+{b*b}={c*c}-1')
  return 1 if a*a + b*b == c*c - 1 and a+b+c <= P else 0

t = 0

cachePrimes(maxA)
storeTimes = 1000
resetTime()
mm=1+2**.5
for a in range(1, maxA + 1):
  for b in range(a, P-a+1):
    for c in range(b, P-b-a+1):
      if check(a, b, c):
        t +=1
  
print(t)

elapsed()
