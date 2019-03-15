import math
import time

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
  lim = int(n  ** .5)
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

def lineNo():
  import inspect
  import ntpath
  info = inspect.stack()[1][0]
  return f'{ntpath.basename(info.f_code.co_filename)}({info.f_lineno}): '


# calc prime numbers from N to M in portions at once (by sieve)
def primesN2M(n = 0, m = 0, portion = 100000):
  if m <= primes[-1]: # check precalculated to simplify
    for p in primes:
      if p < n:
        continue
      if p <= m:
        yield p
      else:
        return
    return
  if m - n > portion: 
    for k in range(n, m + 1, portion):
      for p in primesN2M(k, k + min(portion - 1, m - k), portion):
        yield p
    return
  if n == 0: # ignore 0 and 1
    n = 2

  if m < n or m < 2:
    return

  sieve = [1] * (m - n + 1)
  for i in primesN2M(2, int(m ** .5), portion): # call recursively
    for j in range(max(2, -(-n // i)) * i, m + 1, i):
      sieve[j - n] = 0
  for i in range(len(sieve)):
    if sieve[i]:
      yield n + i

startTime = time.perf_counter()
def elapsed():
  print(f'elapsed_time={time.perf_counter() - startTime:0.3f}')
