maxCalls = 10000000
userCount = 1000000
needFriends = userCount - userCount // 100 # 99%
k = 0
S = [0] * (maxCalls + 1)
def laggedFib():
  global k, S
  while True:
    k += 1
    if S[k] == 0:
      if k <= 55:
        S[k] = (100003 - 200003 * k + 300007 * k**3) % 1000000
      else:
        S[k] = (S[k-24] + S[k-55]) % 1000000
    yield S[k]

def records():
  nums = laggedFib()
  while True:
    yield (next(nums), next(nums))

def join(u1s, u2s):
  if not u1s:
    return u2s
  for i in range(len(u1s)):
    u1 = u1s[i]
    u2 = u2s[i]
    if u2:
      if not u1:
        u1 = u2
      else:
        u1.update(u2)
      for f in list(u2):
        if u1s[f]:
          u1.update(u1s[f])
        u1s[f] = u1

  return u1s

def calc(pm, mcalls):
  users = [None] * userCount
  calls = 0
  maxLen = 0
  gr = 0
  gr1 = 0
  gr2 = 0
  dup = 0
  for u1, u2 in records():
    if calls >= mcalls:
      return users
    if users[pm] and len(users[pm]) >= needFriends:
      print(f'PM is a common friend after {calls} calls')
      return 
    if u1 == u2:
      continue
    calls += 1     
    if calls % 1000 == 0:
      print(f'calls={calls} gr={gr} (+{gr1}-{gr2}) dup={dup} maxLen={maxLen} pm friends={len(users[pm]) if users[pm] else 0} time={time.perf_counter() - t:0.3f}')
      gr1 = 0
      gr2 = 0
      dup = 0

    g1 = users[u1]
    g2 = users[u2]
    if g1 and g1 == g2:
      dup += 1
      continue

    if not g1:
      g1 = set([u1])
      gr += 1
      gr1 += 1
      users[u1] = g1
    if g2:
      if len(g2) > len(g1):
        g1, g2 = g2, g1
        u1, u2 = u2, u1
      g1.update(g2)
      gr2 += 1
      gr -= 1
      for u in g2:
        users[u] = g1
    else:
      g1.add(u2)
      users[u2] = g1

    maxLen = max(maxLen, len(g1))

import time
t = time.perf_counter()

maxs = maxCalls
step = maxs #5000000
u = []
for calls in range(0, maxs, step):
  u = join(u, calc(524287, step))
  mlen = max([len(g) for g in u if g])
  print(mlen)

#for g in u:
#  if g and len(g) == mlen:
#    print(g)

print(f'elapsed_time={time.perf_counter() - t:0.3f}')
