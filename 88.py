from itertools import count

# get all combinations of factorization for 'a'
def calcNumDivs(a, m = 2):
  res = [[a]]
  for p in count(m):
    if p * p > a:
      break;
    if a % p == 0:
      res = res + [[p] + i for i in calcNumDivs(a // p, p)]
  return res

maxk = 12000
maxa = maxk * 2 # init value we never exceed
mina = [maxa for x in range(maxk)] # we will store the solutions here
cnt = 1

for a in count(2):
  # here we search for all factorizations of 'a' and add as many '1's to make it a full sum
  for s in calcNumDivs(a)[1:]: # (skip trivial element [0] == a)
    k = a - sum(s) + len(s) - 1 # number of numbers to give product-sum equal 'a' (-1 to simplify array addressing)
    if k < maxk and mina[k] == maxa: # store the first 'a' found for this 'k'
      mina[k] = a
      cnt += 1
  if cnt == maxk:
    break
print(sum(set(mina[1:]))) # skip k=1