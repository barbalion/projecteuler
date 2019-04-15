# 217 is a prime number. In order 2017 to be a divisor of for sigma(a)=Product((p**(n+1)-1) // (p-1) for all divisors) it must be a power of a prime with (p**(a+1)-1) // (p-1) % 2017 == 0
# so we need only to check all such primes 'p' and count all k*p for k=1..N//p. We check p^n with n>=2 by brute force all primes. For n = 1 we generate all candidates by the formula p = k*2017-1 and check if it's a prime in a effective way.
# we also take care of duplicates when p'=k*p is not a qualified number if k is a qualified number itself.
from tools import *
from math import ceil

def sig(f):
  P = 1
  for p,a in f:
    P *= (p**(a+1)-1) // (p-1)
  return P

err = 1e-10

def calc(N, D):
  def check(n):
    return not sig(factor(n)) % D
  cachePrimes(int(N**.5))
  def a2n(a):
    return (a + 1) // D
  from math import log
  def genPrimeSigDivs(minA, maxA): # generate all primes and primes**k with sig % 2017 == 0
    if minA > maxA:
      return None
    maxE = int(ceil(log(maxA)/log(2)))
    for e in range(2, maxE): # for power >= 2 check all primes
      for p in primesN2M(ceil(minA**(1/e)-err), int(maxA**(1/e)+err)):
        if ((p**(e+1)-1) // (p-1)) % D == 0:
          yield p, e

    for n in range(ceil((minA + 1)/D-err), (maxA+1)//D+1): # for power==1 check all 2017*k-1 for primality
      p = n * D - 1
      if isPrimeMillerRabin(p, 5): 
        yield p, 1

  def excl(p, e, N=N):
    a = p**e
    mem = set(range(0, N+1, a*p))

    for p2, e2 in genPrimeSigDivs(a+1, N//a):
      ex2 = excl(p2, e2, N//a)
      for a2 in range(0, N+1, a*p2**e2):
        k2 = a2//a
        if check(k2) and not k2 in ex2 and not a2 in mem:
          mem.add(a2)
    return mem

  elapsed()
  resetTime()

  res = 0
  for p, e in genPrimeSigDivs(D-1, N): # walk though all qualified primes**e
    a = p**e
    k = N // a
    res += a*k*(k + 1) // 2 # sum of all qualified numbers
    res -= sum(excl(p, e))

    if a % 10000 == 1:
      elapsed((a, 1, N))
  return res

print(calc(10**11, 2017))

elapsed()
