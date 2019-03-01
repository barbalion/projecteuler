from tools import *
from itertools import count
import time

t = time.perf_counter()

limit = 1000000
i = 0
ml, ms = 0, 0
ss = 0
while ss < limit:
  s = ss
  for j in count(i + ml):
    s += primeN(j)
    if s > limit:
      break
    if s >= ms and j - i >= ml and isPrime(s):
      ml, ms = j - i, s
      ss = s - primeN(j)
      result = f'max prime: {s}, prime count: {j-i+1} (from {i} to {j})'

  ss += primeN(i + ml) - primeN(i)
  i +=1

print(result)
print(f'elapsed_time={time.perf_counter() - t:0.3f}')
