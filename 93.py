ops = {
  '+': lambda a, b: [a + b],
  '-': lambda a, b: [a - b],
  '*': lambda a, b: [a * b],
  '/': lambda a, b: [a / b] if b != 0 else []
}

def calcall(d):
  res = []

  def calc(d):
    if len(d) <= 1:
      return d
    return sum([ops[op](a, b) for op in ops for i in range(1, len(d)) for a in calc(d[0:i]) for b in calc(d[i:])], [])

  for i0 in range(4):
    for i1 in range(4):
      for i2 in range(4):
        for i3 in range(4):
          if i0 != i1 and i0 != i2 and i0 != i3 and i1 != i2 and i1 != i3 and i2 != i3:
            res = res + calc([d[i0], d[i1], d[i2], d[i3]])

  return res

maxn = 0

for a in range(1, 10):
  for b in range(a + 1, 10):
    for c in range(b + 1, 10):
      for d in range(c + 1, 10):
        abcd = a * 1000 + b * 100 + c * 10 + d
        al = calcall([a, b, c, d])
        for n in range(1, len(al)+2):
          if not list(filter(lambda x: abs(n - x) < 1e-6, al)):
            if n > maxn:
              maxn = n
              print(abcd, n - 1)
            break
