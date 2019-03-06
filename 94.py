def calcSquarePerim(a, d):
  ar = (a * 3 + d)*(a - d) # core to check from Heron's formula 
  return a * 3 + d if int(ar ** .5) ** 2 == ar else 0

maxp = 1000000000
res = 0
for a in range(2, int(maxp ** .5 / 3) + 1):
  # check only the proper candidates (were found empirically, however can be strictly proven)
  res += calcSquarePerim(a ** 2 + 1, 1) + calcSquarePerim(a ** 2 * 2 - 1, -1)

print(res)