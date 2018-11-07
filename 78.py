import math
mem = []

modulus = 10**6

def p(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  # prep memory
  for i in range(n-len(mem)+1):
    mem.append(0)
  # check in the mem
  if mem[n] > 0:
    return mem[n]
  res = 0
  for k in range(-int((math.sqrt(24*n+1)-1)/6), int((math.sqrt(24*n+1)+1)/6)+1):
    if k == 0:
      continue
    g = k*(3*k-1)//2
    s = 1 if (abs(k)-1) % 2 == 0 else -1
    res += s * p(n - g)

  res %= modulus

  #put the result into the memory and return
  mem[n] = res
  return res
    
for n in range(1, 60000):
  pn = p(n)
  print(n, pn, end='\r') 
  if pn % modulus == 0:
    print(n, '          ') 
    break
