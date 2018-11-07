m  = 0
for i in (range(100, 1000)):
  for j in (range(i, 1000)):
    p = i*j
    if p > m and str(p)[::-1] == str(p):
      m = p
print(m)
