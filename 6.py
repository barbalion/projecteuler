lim = 100
s1, s2 = 0, 0
for i in range(1, lim+1):
  s1 += i * i
  s2 += i
print(s2*s2 - s1)
