#Fibonachi
c = 1
a, b = 0, 1
while b <= 10**999:
  a, b = b, a + b
  c += 1

print(c, len(str(a)), len(str(b)))
