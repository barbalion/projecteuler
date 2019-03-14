def laggedFib():
  S = [0] * 10000000
  for k in range(1, min(56, len(S))):
    S[k] = (100003 - 200003 * k + 300007 * k**3) % 1000000
    yield S[k]
  k = 56
  while True:
    S[k] = (S[k-24] + S[k-55]) % 1000000
    yield S[k]
    k += 1

def records():
  n = 1
  nums = laggedFib()
  while True:
    yield (next(nums), next(nums))
    #from random import randint
    #yield (randint(0, 99999), randint(0, 99999))
    n += 1


def calc(pm):
  users = [None] * 1000000 #for i in range(1000000)]
  calls = 0
  maxLen = 0
  gr = 0
  gr1 = 0
  gr2 = 0
  dup = 0
  for u1, u2 in records():
    if u1 == u2:
      continue
    calls += 1     
    if calls % 1000 == 0:
      print(f'calls={calls}, gr={gr} (+{gr1}-{gr2}), dup={dup}, maxLen={maxLen}')
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
      g1.update(g2)
      gr2 += 1
      gr -= 1
      for u in g2:
        users[u] = g1
    else:
      g1.add(u2)
      users[u2] = g1

    maxLen = max(maxLen, len(g1))

    if calls == 5000000:
      return

import time
t = time.perf_counter()

calc(524287)

print(f'elapsed_time={time.perf_counter() - t:0.3f}')
