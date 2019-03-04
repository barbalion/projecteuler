from functools import reduce
from itertools import count

ops = {
  '+': lambda a, b: [a + b], 
  '-': lambda a, b: [a - b], 
  '*': lambda a, b: [a * b], 
  '/': lambda a, b: [a / b] if b != 0 else []}

def calcall(d):
  def calc(d):
    if len(d) <= 1:
      return d
    return sum([ops[op](a, b) 
      for op in ops for i in range(1, len(d)) 
      for a in calc(d[0:i]) 
      for b in calc(d[i:])], [])
  return sum([calc([d[i0], d[i1], d[i2], d[i3]]) 
    for i0 in range(4) 
    for i1 in range(4) 
    for i2 in range(4) 
    for i3 in range(4) 
    if i0 != i1 and i0 != i2 and i0 != i3 and i1 != i2 and i1 != i3 and i2 != i3], [])

maxn = 0
for d in [[a, b, c, d] for a in range(1, 10) for b in range(a + 1, 10) for c in range(b + 1, 10) for d in range(c + 1, 10)]:
  al = calcall(d)
  for n in count(1):
    if not [n for x in al if abs(n - x) < 1e-6]:
      if n > maxn:
        maxn = n
        print(d, n - 1)
      break
