from math import *
def largestPrimeDiv(n):
  for i in range(int(sqrt(n)), 1, -1):
    if n % i == 0 and largestPrimeDiv(i) == 1:
      return i
  return 1
print(largestPrimeDiv(600851475143))
