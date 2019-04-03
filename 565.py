from tools import *

def calc(N, D):
  if N > 1000:
    cachePrimes(int(N**.5))
  res = 0
  for n in range(1, N+1):
    ds = divs(n)
    s = sum(ds)
    if s % D == 0:
      res += n
      print(n, res, n/D, n%D)
    if n % 100000 == 0:
      elapsed((n, 1, N))
  return res

print(calc(10**7, 2017))