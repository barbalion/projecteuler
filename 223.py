from tools import *
P = 25000

def check(a, b, c):
#  if a*a + b*b == c*c + 1 and a+b+c <= P:
#    print(f'{a},{b},{c}: {a*a}+{b*b}={c*c}+1')
  return 1 if a*a + b*b == c*c + 1 and a+b+c <= P else 0

t = (P - 1) // 2 # {1, n, n} is allways a solution, just skip it
#for a in range(1, t+1): # for debug only
#  check(1, a, a)

resetTime()
it = 0
maxN = int((18**.5-4)*P / 2) + 1 # approx n when minA > maxA
for n in range(1, maxN): 
  minA = int((2*n**2+1)**.5+n+.5)
  maxA = int(((n**2+4*n*P+4)**.5-n)/2)
#  if minA > maxA:
#    break
#  t = 0
  for a in range(minA + (minA + n + 1)%2, maxA + 1, 2):
    it += 1
    if (a**2-1-n**2) % (2*n) == 0:
      t +=1
#    b = (a**2-1-n**2)//(2*n)
#    c = (a**2-1+n**2)//(2*n)
#    print(n, a,b,c)
#    if check(a, b, c):
#      print(n, a, b, c)
#      t += 1
#      print(a, b, c, n)
#  print('=====',n, minA, maxA, t)
  if n % 100 == 0:
    elapsed((n, 1, maxN))

print(t, it)

elapsed()