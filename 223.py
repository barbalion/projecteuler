from tools import *
P = 50000

t = (P - 1) // 2 # {1, n, n} is allways a solution, just skip it

resetTime()
maxN = int((18**.5-4)*P / 2) + 1 # approx n when minA > maxA
for n in range(1, maxN): 
  minA = int((2*n**2+1)**.5+n+.5)
  maxA = int(((n**2+4*n*P+4)**.5-n)/2)
  for a in range(minA + (minA + n + 1)%2, maxA + 1, 2):
    if n % 2 == 0:
      if (a**2-1) % (2*n) == 0:
        t +=1
    else:
      if (a**2-1) % n == 0:
        t +=1
  if n % 100 == 0:
    elapsed((n, 1, maxN))

print(t)

elapsed()