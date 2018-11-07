from tools import *
minP, maxP = 0, 0
while True:
  p = primeN(maxP)
  if p > 1000 and minP ==0:
    minP = maxP
  if p > 10000:
    break
  maxP += 1
for i in range(minP, maxP):
  p = primeN(i)
  for j in range(1, (10001 - p)//2):
    p2 = p + j
    p3 = p + j + j
    if isPrime(p2) and isPrime(p3):
      if set(str(p)) == set(str(p2)) and set(str(p2)) == set(str(p3)):
        print(p, p2, p3, j, str(p)+str(p2)+str(p3))
