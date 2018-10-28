def fact(n):
  p = 1
  for i in range(2, n+1):
    p = p * i
  return p


print(sum([int(i) for i in str(fact(100))]))

#print(fact(10))