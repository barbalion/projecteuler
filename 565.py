# 217 is a prime number. In order 2017 to be a divisor of for sigma(a)=Product((p**(n+1)-1) // (p-1) for all divisors) it must be a power of a prime with (p**(a+1)-1) // (p-1) % 2017 == 0
# so we need only to check all such primes 'p' and count all k*p for k=1..N//p. We check p^n with n>=2 by brute force all primes. For n = 1 we generate all candidates by the formula p = k*2017-1 and check if it's a prime in a effective way.
# we also take care of duplicates when p'=k*p is not a proper number if k is a proper number itself.
from tools import *

def calc(N, D):
  cachePrimes(int(N**.5))
  def a2n(a):
    return (a + 1) // D
  def genPrimeSigDivs(n, m): # generate all primes and primes**k with sig % 2017 == 0
    if n > m:
      return None
    for e in range(2, 5): # for power > 2 check all primes
      for p in primesN2M(int((n*D-1)**(1/e))+1, int((m*D-1)**(1/e))):
        a = p**e
        if ((p**(e+1)-1) // (p-1)) % D == 0:
          yield a
    for n in range(n, m+1): # for power==1 check all 2017*k-1 for primality
      a = n * D - 1
      if isPrimeMillerRabin(a): 
        yield a

  elapsed()
  resetTime()

  res = 0
  for a in genPrimeSigDivs(1, a2n(N)): # walk though all proper primes**n
    k = N // a # count of rated numbers
    res += a*k*(k + 1) // 2 # sum of all rated numbers

    for aa in genPrimeSigDivs(a2n(a), a2n(k)):
      for dup in range(0, N, aa*a):
        res -= dup

    if a % 1000 == 1:
      elapsed((a, 1, N))
  return res

print(calc(10**9, 2017))

elapsed()
