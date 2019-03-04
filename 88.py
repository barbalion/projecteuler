from tools import *
from itertools import count
from functools import reduce
import time
import sys

numdivs={}

def calcNumDivs(a):
  if a in numdivs:
    return numdivs[a]
  divs = [1]
  for p in count(2):
    if p * p > a:
      break;
    if a % p == 0:
      divs += [p, a // p]
  divs.sort()
  numdivs[a] = divs
  return divs

mem = {}
hits = 0
miss = 0 
mem2 = [sys.maxsize for x in range(12001)]

def checkSum(a, am, k, i, nums, dep=0):
  if i >= len(nums) or k == 0:
    return False

  if a < nums[i] or am < nums[i] or a > am * k: #is the nums are ordered accending
    return False

  if a == nums[i] * k and am == nums[i] ** k:
    return True

  if k == 1:
    return a == nums[i] and am == nums[i]

  s = f'{a},{am},{k}'
  if s in mem:
    global hits, miss
    hits += 1
    return mem[s]
  miss += 1

  #print(' '* dep, a, am, k, i)
  tr = (am % nums[i] == 0 and checkSum(a - nums[i], am // nums[i], k-1, 0, nums, dep+1)) or checkSum(a, am, k, i+1, nums, dep+1)

  mem[s] = tr
  return tr

def checkSum2(a, am, k, i, nums, dep=''):
  if i >= len(nums) or k == 0:
    #print('fintro', a, am, k, i)
    return []

  if a == nums[i] * k and am == nums[i] ** k:
    #print('pow')
    return [nums[i]] * k

  s = f'{a},{am},{k}'
  if s in mem:
    return mem[s]
  
  #print(dep, f'a={a}, am={am}, k={k}, i={i}', nums)
  if am % nums[i] == 0:
    tr = checkSum2(a - nums[i], am // nums[i], k-1, 0, nums, dep+f'{nums[i]}+')
    if tr:
      tr = [nums[i]] + tr
  else:
    tr = []
    #print('skipstep')
  if not tr:
    tr = checkSum2(a, am, k, i+1, nums, dep+'--')
  mem[s] = tr
  return tr


a = 348
k = 174
mem = {}
print(k, a, checkSum2(a, a, k, 0, calcNumDivs(a)), len(mem))
mem = {}

sys.setrecursionlimit(20000)

res = set()
t = time.perf_counter()
for k in range(2000, 2200):
  for a in range(k+2, 2*k+1):
    if mem2[k] <= a:
      #print('s', k, a, mem2[k])
      break
    s = checkSum(a, a, k, 0, calcNumDivs(a))
    if s:
      print(k, a, s, f'{time.perf_counter() - t:0.3f}', len(mem), hits, miss)
      #t = time.perf_counter()
      res.add(a)
      if a > 2*k: 
        print(k, a, k + math.sqrt(k),k*k) 
        1/0
      break;
print(f'elapsed_time={time.perf_counter() - t:0.3f}')

#print(mem)
#print(hits, miss)

#print(res)
#print(mem2)