maxP = 25000000
squares = [x**2 for x in range(1, int(maxP ** .5))]
cnt = len(squares)

t = 0
for i in range(cnt):
  print(i)
  for j in range(i, cnt):
    for k in range(j, cnt):
      a = squares[i]
      b = squares[j]
      c = squares[k]
      p = a +b +c
      if a + b == c + 1 and p <= maxP:
        t +=1
print(t)