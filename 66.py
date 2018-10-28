import operator, functools
import math, pdb
import sys
from decimal import *

def isPr(a):
  for i in range(2, int(math.sqrt(a) + 1)):
     if a % i == 0:
       return False
  else:
    return True

def divNum(a):
  c = 0
  for i in range(1, int(math.sqrt(a) + 1)):
     if a % i == 0:
       c += 1
       if i * i != a:
         c += 1
#       print(a, i, c)
  return c

def fact(a):
  if a <= 2:
    return a
  else:
    return a * fact(a-1)

mx = 1
md = 0
#import pdb; pdb.set_trace()

with localcontext() as ctx:
  def appr(m, n):
    im = Decimal(m).quantize(Decimal('1'), rounding=ROUND_DOWN)
    if im==m or n == 1:
      return (m.quantize(Decimal('1'), rounding=ROUND_HALF_UP), 1)
    else:
      (a, b) = appr(Decimal(1)/(Decimal(Decimal(m)-im)), n-1)
      #print(im, m-im, im*a+b, a, b)
      return (im*a+b, a)

  for d in range(1, 10010):
    if d//int(math.sqrt(d))==math.sqrt(d):
      continue
    x = 0
    y = 0

    ctx.prec = 10
    while True:
      for n in range(2, ctx.prec):
        (x, y) = appr(Decimal(d).sqrt(), n)
        if x*x-d*y*y==1:
          print(d, x, y, ctx.prec)
          break
      else:
        x = 0
        ctx.prec = ctx.prec * 2
        continue
      break

    if x > mx:
      mx = x
      md = d 
    print("d=", d, "mx=", mx, md, ctx.prec)
