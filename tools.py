import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

def isPrime(n):
  i = 0
  lim = int(math.sqrt(n))
  while primeN(i) <= lim:
    if n % primeN(i) == 0:
      return False
    i += 1
  return True

def primeN(n):
  p = primes[-1]
  while True:
    if n < len(primes):
      return primes[n]
    p += 2
    if isPrime(p):
      primes.append(p)

def allPrimes():
  n = 0
  while True:
    yield primeN(n)
    n += 1
    
def factor(n):
  res = []
  p = 2
  lim = int(math.sqrt(n))
  while n > 1 and p < lim:
    if n % p == 0:
      if len(res) == 0 or res[-1][0] != p:
        res += [[p, 0]]
      res[-1] = [p, res[-1][1]+1]
      n = n // p
      lim = int(math.sqrt(n))
      continue
    if p > 2:
      p += 2
    else:
      p += 1
  return res  


def gcd(m, n):
  while m % n != 0:
    m, n = n, m % n
  return n 
