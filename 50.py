from tools import *
import time

t = time.perf_counter()

limit = 1000000
i = 0
ml, ms = 0, 0
ss = 0
while ss < limit:
  s = ss
  j = i + ml
  while True:
    s += primeN(j)
    if s > limit:
      break
    if s >= ms and j - i >= ml and isPrime(s):
      ml, ms = j - i, s
      ss = s - primeN(j)
      result = f'max prime: {s}, prime count: {j-i+1}, (from {i} to {j})'
    j +=1

  ss += primeN(i + ml) - primeN(i)
  i += 1

print(result)
print(f'elapsed_time={time.perf_counter() - t:0.3f}')
