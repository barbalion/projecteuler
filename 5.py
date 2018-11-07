from tools import *
s = 1
for i in (range(1, 21)):
  s *= i // gcd(s, i)
print(s)
