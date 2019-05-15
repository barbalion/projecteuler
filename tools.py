import math
import time

def gcd(m, n):
  while m % n != 0:
    m, n = n, m % n
  return n 

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

def isPrime(n):
  i = 0
  lim = int(math.sqrt(n))
  while primeN(i) <= lim:
    if n % primeN(i) == 0:
      return False
    i += 1
  return True

def isPrimeFerma(n):
  return pow(37, n-1, n) == 1 and pow(59, n-1, n) == 1 and pow(83, n-1, n) == 1

from random import randrange
def isPrimeMillerRabin(n, k=5):
  if n == 2:
    return True
  if not n & 1:
    return False
  def check(a, s, d, n):
    x = pow(a, d, n)
    if x == 1:
      return True
    for i in range(s - 1):
      if x == n - 1:
        return True
      x = pow(x, 2, n)
    return x == n - 1
  s = 0
  d = n - 1
  while d % 2 == 0:
    d >>= 1
    s += 1
  for i in range(k):
    a = randrange(2, n - 1)
    if not check(a, s, d, n):
      return False
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

factorMem = {1:[]}
maxNFactorMem = 1000000
def factor(n, precalculatePrime=False):
  if n < maxNFactorMem and n in factorMem:
    return factorMem[n]
  a = n
  if precalculatePrime:
    cachePrimes(int(a**.5))
    print(a)
    elapsed()
  for p in primesN2M(2, int(a ** .5)):
    cnt = 0
    while a % p == 0:
      cnt += 1
      a = a // p
    if cnt > 0:
      res = [[p, cnt]] + factor(a)
      if n < maxNFactorMem:
        factorMem[n] = res
      return res
  res = [[n, 1]]
  if n < maxNFactorMem:
    factorMem[n] = res
  return res

# calc prime numbers from N to M in portions at once (by sieve)
def primesN2M(n = 0, m = 0, portion = 100000, doYield = True):
  if n > m:
    return
  global primes
  addToMem = []
  if doYield and n <= primes[-1]: # check precalculated to simplify
    for p in primes:
      if p < n:
        continue
      if p <= m:
        yield p
      else:
        return
    addToMem = [primes[-1]]
    n = primes[-1] + 1

  if m - n > portion: 
    for k in range(n, m + 1, portion):
      for p in primesN2M(k, k + min(portion - 1, m - k), portion, doYield):
        if doYield:
          yield p
  else:
    if n == 0: # ignore 0 and 1
      n = 2

    if m < n or m < 2:
      return
    sieve = [1] * (m - n + 1)
    for i in primesN2M(2, int(m ** .5), portion, True): # call recursively
      for j in range(max(2, -(-n // i)) * i, m + 1, i):
        sieve[j - n] = 0
    for i in range(len(sieve)):
      if sieve[i]:
        if addToMem or n + i == primes[-1]:
          addToMem += [n+i]
        if doYield:
          yield n + i

    if len(addToMem) > 1 and primes[-1] == addToMem[0]:
      primes += addToMem[1:]
  if not doYield:
    yield None

def cachePrimes(n):
  if n > primes[-1]:
    next(primesN2M(primes[-1], n, n, False))

def primeAsSumOfSquares(p):
  if p == 2:
    return (1, 1)
  cachePrimes(int(p**.25))
  if p % 4 != 1:
    return None
  # as described at https://www.alpertron.com.ar/4SQUARES.HTM
  p2 = (p-1)//2
  for a in allPrimes(): 
    if pow(a, p2, p) == p-1:
      break
  a, b = pow(a, p2//2, p), 1
  while True:
    k = (a*a + b*b) // p
    if k == 1:
      return (abs(b), abs(a))
    a1, b1 = (a + k//2) % k - k//2, (b + k//2) % k - k//2
    a, b = (a * a1 + b * b1) // k, (a * b1 - b * a1) // k

def isDivC(x1, x2):
  a1, b1, a2, b2 = x1.real, x1.imag, x2.real, x2.imag
  return (a1*a2+b1*b2) % (a2**2+b2**2) == 0 and (a2*b1-a1*b2) % (a2**2+b2**2) == 0
def divC(x1, x2):
  a1, b1, a2, b2 = x1.real, x1.imag, x2.real, x2.imag
  return (a1*a2+b1*b2) // (a2**2+b2**2) + (a2*b1-a1*b2)//(a2**2+b2**2)*1j

def asSumOfSquares(c):
  for a in range(int((c/2)**.5)+1):
    b = int((c - a**2)**.5)
    if a*a+b*b==c:
      return (a,b)
  return None

def factorC(c):
  res = []
  norm = int(c.real)**2+int(c.imag)**2
  for p, n in factor(norm):
    if p % 4 == 3: # prime by it self
      res += [(p, n//2)]
      c = divC(c, p ** (n//2))
    else: # p % 4==1 or p==2 - decomposing in to 2 conjugate primes
      a, b = primeAsSumOfSquares(p)
      for d in [a+1j*b, b+1j*a]:
        for n2 in range(0, n+1):
          if isDivC(c, d):
            c = divC(c, d)
          else:
            if n2 > 0:
              res += [(d, n2)]
            break
  return [(c, 1)] + res

def poly2EtaGuessLeastSq(res, lastTimes):
  if len(lastTimes)<4:
    return res
  n, xm = len(lastTimes)-1, lastTimes[-1][0][2] # skip first point because it's usually very inacurate
  xs, ys = [p[0][0] for p in lastTimes[1:]], [p[1] for p in lastTimes[1:]]
  sx1, sx2, sx3, sx4 = sum([x for x in xs]), sum([x*x for x in xs]), sum([x**3 for x in xs]), sum([x**4 for x in xs])
  sxy, sx2y, sy = sum([x*y for x, y in zip(xs, ys)]), sum([x*x*y for x, y in zip(xs, ys)]), sum([y for y in ys])
  a = (sx1**2*sx2y - n*sx2*sx2y + n*sx3*sxy + sx2**2*sy - sx1*(sx2*sxy + sx3*sy))/(sx2**3 + n*sx3**2 + sx1**2*sx4 - sx2*(2*sx1*sx3 + n*sx4))
  b = (-(sx1*sx2*sx2y) + n*sx2y*sx3 + sx2**2*sxy - n*sx4*sxy - sx2*sx3*sy + sx1*sx4*sy)/(sx2**3 + n*sx3**2 + sx1**2*sx4 - sx2*(2*sx1*sx3 + n*sx4))
  c = (sx2**2*sx2y - sx1*sx2y*sx3 + sx1*sx4*sxy + sx3**2*sy - sx2*(sx3*sxy + sx4*sy))/(sx2**3 + n*sx3**2 + sx1**2*sx4 - sx2*(2*sx1*sx3 + n*sx4))
  ym = a*xm*xm + b*xm + c
  return res[:-1] + (ym - res[0],)

startTime = 0
prevTime = 0
lastTimes = []
storeTimes = 50
def resetTime():
  global startTime,lastTimes
  startTime = time.perf_counter()
  prevTime = time.perf_counter()
  lastTimes = []

resetTime()
def elapsed(pos=None, doPrint = True, timeGuess=poly2EtaGuessLeastSq, s=None):
  global lastTimes, prevTime
  res = (time.perf_counter() - startTime, time.perf_counter() - prevTime, 0)
  prevTime = time.perf_counter()
  if pos and len(pos) == 3:
    curr = pos[0]-pos[1]
    maxP = pos[2]-pos[1]
    if curr == 0:
      curr = 1

    if len(lastTimes) >= storeTimes:
      lastTimes = lastTimes[1:storeTimes]
    lastTimes += [(pos, time.perf_counter() - startTime)]

    res = (res[0], res[1], ((time.perf_counter() - startTime)*(maxP-curr))/curr)
    if timeGuess:
      res = timeGuess(res, lastTimes)

  if doPrint:
    if pos:
      print(f'pos={s if s else pos[0]} ({(100*(pos[0]-pos[1])/(pos[2]-pos[1])):0.2f}%) prev={res[1]:0.3f}s, total={res[0]:0.0f}s, eta={res[2]:0.0f}s', flush=True)
    else:
      print(f'{s+" " if s else ""}Elapsed time={res[0]:0.3f}', flush=True)
  return res

def divs(a):
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
  return res    

perflog = {}
lastPerf = time.perf_counter()
def pref(id):
  t, lastPerf = time.perf_counter() - lastPerf, time.perf_counter()
  if id in perflog:
    t += perflog[id]
  perflog[id] = t    

def printPref():
  print(perflog)

def lineNo():
  import inspect
  import ntpath
  info = inspect.stack()[1][0]
  return f'{ntpath.basename(info.f_code.co_filename)}({info.f_lineno}): '
