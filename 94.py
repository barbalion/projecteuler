from itertools import count
import math

maxp = 1000000000

ap1s = set() # store a, a, a+1
am1s = set() # store a, a, a-1

# Heron's formula for integer colculation, return area^2*16
def area216(a, b, c):
  p = (a + b + c)
  return p*(p-2*a)*(p-2*b)*(p-2*c)

# fast integer sqrt
def isqrt(n):
  x = n
  y = (x + 1) // 2
  while y < x:
      x = y
      y = (x + n // x) // 2
  return x
    
def check(a, d, s):
  ar = area216(a, a, a+d)
  t = int(math.sqrt(ar // 16))
  if t * t * 16 == ar:
    s.add(a) 
    print(a, d, t)

for a in range(2, maxp // 3 + 1):
  check(a, 1, ap1s)
  check(a, -1, am1s)
  if a % 1000000 == 0:
    print(a)

print(sum([a*3+1 for a in ap1s])+sum([a*3-1 for a in am1s]))