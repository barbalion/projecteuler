def C(n, r):
  t = 1
  for i in range(n, 0, -1):
    if i > r:
      t *= i
    if i <= n - r:
      t //= i
  return t

to = 0
for n in range(1, 101):
  for r in range(1, n+1):
    if C(n, r) > 1000000:
      to += 1

print(to)    