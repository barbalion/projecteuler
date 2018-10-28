import math, pdb

def P(r, n):
  return int(n*((r-2)*n-(r-4))/2)

def invP(r, P):
  return (-4 + r + math.sqrt(16 - 16*P - 8*r + 8*P*r + r*r))/(2.*(-2 + r))

maxR=8
needLen=6

nums = [[] for _ in range(3, maxR+1)]
for r in range(3, maxR+1):
  p = 0
  n = 1
  while p < 10000:
    p = P(r, n)
    if p>=1000 and p<10000:
      nums[r-3].append(p)
    n += 1

def find(r, st=[]):
  nu = nums[r-3]
  for n in range(len(nu)):
    p = nu[n]
    if len(st) == 0 or p // 100 == st[-1][2] % 100:
      stn = st + [[r, n, p]]
      if len(stn) == needLen:
        if stn[0][2] // 100 == stn[-1][2] % 100:
          print(stn, sum([s[2] for s in stn]))
      else:
        for rn in range(3, maxR+1):
          if len([s for s in stn if s[0]==rn]) == 0:
            find(rn, stn)
        
find(3, [])
