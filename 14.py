m = 0
mi = 0

def nex(a):
  if a % 2 == 0:
    return a // 2
  else:
    return a * 3 + 1

for i in range(3, 1000001):
  x = i
  c = 1
  while x > 1:
    c += 1
    x = nex(x)
  if c > m:
    m = c
    mi = i
    print(i, c, m, mi)
