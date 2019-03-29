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

factorMem = {1:[]}
def factor(n):
  if n in factorMem:
    return factorMem[n]
  a = n
  for p in primesN2M(2, int(a ** .5)):
    cnt = 0
    while a % p == 0:
      cnt += 1
      a = a // p
    if cnt > 0:
      res = [[p, cnt]] + factor(a)
      factorMem[n] = res
      return res
  res = [[n, 1]]
  factorMem[n] = res
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
def primesN2M(n = 0, m = 0, portion = 100000, doYield = True):
  if m < n:
    return
  global primes
  if n <= primes[-1]: # check precalculated to simplify
    for p in primes:
      if p < n:
        continue
      if p <= m:
        if doYield:
          yield p
      else:
        n = p
        break

  addToMem = []
  if m - n > portion: 
    for k in range(n, m + 1, portion):
      for p in primesN2M(k, k + min(portion - 1, m - k), portion, doYield):
        if p == primes[-1] or addToMem:
          addToMem += [p]
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
        if n + i == primes[-1] or addToMem:
          addToMem += [n+i]
        if doYield:
          yield n + i
  if len(addToMem) > 1 and primes[-1] == addToMem[0]:
    primes += addToMem[1:]
  if not doYield:
    yield []

def cachePrimes(n):
  next(primesN2M(2, n, n, False))

def poly2EtaGuessLeastSq(res, lastTimes):
  if len(lastTimes)<3:
    return res
  n, xm = len(lastTimes), lastTimes[-1][0][2]
  xs, ys = [p[0][0] for p in lastTimes], [p[1] for p in lastTimes]
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
def elapsed(pos=None, doPrint = True, timeGuess=poly2EtaGuessLeastSq):
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
      print(f'pos={pos[0]} prev={res[1]:0.3f}s, total={res[0]:0.0f}s, eta={res[2]:0.0f}s', flush=True)
    else:
      print(f'elapsed time={res[0]:0.3f}', flush=True)
  return res

