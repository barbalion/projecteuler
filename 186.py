maxCalls = 10000000
userCount = 1000000
needFriends = userCount - userCount // 100 # >= 99%
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

def calc(pm):
  users = [None] * userCount
  calls = 0
  maxLen = 0
  gr, gr1, gr2, dup = 0, 0, 0, 0 # stat
  for u1, u2 in records():
    if u1 == u2:
      continue
    calls += 1     
    if calls % 1000 == 0:
      print(f'calls={calls} gr={gr} (+{gr1}-{gr2}) dup={dup} maxLen={maxLen} pm_friends={len(users[pm]) if users[pm] else 0} time={time.perf_counter() - t:0.3f}')
      gr1 = 0
      gr2 = 0
      dup = 0
    if pm in [u1, u2]:
      print(f'PM got a friend after {calls} calls')

    g1 = users[u1]
    g2 = users[u2]
    if g1 and g1 == g2:
      dup += 1 # stat
      continue

    if not g1:
      g1 = [u1]
      users[u1] = g1
      gr += 1 # stat
      gr1 += 1 # stat
    if g2:
      if len(g2) > len(g1):
        g1, g2 = g2, g1
        u1, u2 = u2, u1
      g1 += g2
      gr2 += 1 # stat
      gr -= 1 # stat
      for u in g2:
        users[u] = g1
    else:
      g1 += [u2]
      users[u2] = g1

    maxLen = max(maxLen, len(g1))
    if g1 == users[pm]:
      print(f'New friend for pm: {len(g1)} at call {calls}')
      g1.sort()
      cnt = 0
      pu = -1
      for u in g1:
        if u != pu:
          cnt += 1
          pu = u
      print(f'        this gives {cnt} unique friends')
      if cnt >= needFriends:
        print(f'PM is a common friend ({cnt}) after {calls} calls')
        return 

import time
t = time.perf_counter()

calc(524287)

print(f'elapsed_time={time.perf_counter() - t:0.3f}')
