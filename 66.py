import operator, functools
import math, pdb
import sys
from decimal import *

mx = 1
md = 0

def appr(m, n):
  im = Decimal(m).quantize(Decimal('1'), rounding=ROUND_DOWN)
  if im==m or n == 1:
    return (m.quantize(Decimal('1'), rounding=ROUND_HALF_UP), 1)
  else:
    (a, b) = appr(Decimal(1)/(Decimal(Decimal(m)-im)), n-1)
    return (im*a+b, a)

for d in range(1, 1001):
  if d//int(math.sqrt(d))==math.sqrt(d):
    continue
  x = 0
  y = 0

  getcontext().prec = 10
  while True:
    for n in range(2, getcontext().prec):
      (x, y) = appr(Decimal(d).sqrt(), n)
      if x*x-d*y*y==1:
        print(d, x, y, getcontext().prec)
        break
    else:
      x = 0
      getcontext().prec = getcontext().prec * 2
      continue
    break

  if x > mx:
    mx = x
    md = d 
  print("d=", d, "mx=", mx, md, getcontext().prec)
