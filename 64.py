import math
from decimal import *
getcontext().prec = 250

def contfr(a, res, err):
  if a * err > 1:
    raise Exception(f"Precision error on {a}: {res}!")
  i = Decimal(int(a))
  d = Decimal(a) - Decimal(i)
  if d == 0:
    return 0
  for n in range(len(res)):
    (i0, d0) = res[n]
    if i == i0 and (d-d0).copy_abs() < err:
      return len(res) - n
  return contfr(Decimal(1)/d, res + [(i, d)], err * a / d)

maxn = 10000
err = Decimal(1) / Decimal(10 ** (getcontext().prec - 2))

print(sum([contfr(Decimal(n).sqrt(), [], err) % 2 for n in range(maxn + 1)]))
