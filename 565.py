from tools import *

def sig(f):
  P = 1
  for p,a in f:
    P *= (p**(a+1)-1) // (p-1)
  return P

def check(n, D):
  return 0 if sig(factor(n)) % D else n

def calc2(N, D, e=0):
  res = 0
  for p in primesN2M(2, int(N**(1/e))+1):
    a = p**e
    s = (p**(e+1)-1) // (p-1)
    if s % D == 0:
      k = N // a
      res += a*k*(k + 1) // 2
      j = k//p
      res -= a*a*j*(j+1)//2
  return res

def calc(N, D):
  cachePrimes(int(N**.5))
  res = 0
  for e in range(2, 5):
    res += calc2(N, D, e)

  ex = set()

  maxN = N//D
  for n in range(6, maxN+1):
    a = n*D - 1
    if isPrime(a):
      k = N // a
      res += a*k*(k + 1) // 2

      for kk in range(a, k+1):
        if check(kk, D) > 1 and not (a*kk in ex):
          res -= a*kk
          ex.add(a*kk)

    if n % 10000 == 1:
      elapsed((n, 1, maxN))
  return res

print(calc(10**11, 2017))

elapsed()