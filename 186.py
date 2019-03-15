maxCalls = 10000000
userCount = 1000000
needFriends = userCount - userCount // 100 # >= 99%
def laggedFib():
  k = 0
  S = [0] * (maxCalls*2 + 1)
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

class llist:
  class litem:
    next = None
    def __init__(self, v):
      self.v = v

    first = None
  last = None
  count = 0

  def __init__(self, v):
    self.add(v)

  def add(self, i):
    li = self.litem(i)
    if self.last:
      self.last.next = li
    else:
      self.first = li
    self.last = li
    self.count += 1
      
  def addAll(self, i):
    if self.last:
      self.last.next = i.first
    else:
      self.first = i.first
    self.last = i.last
    self.count += i.count

  def __iter__(self):
    i = self.first
    while i:
      yield i.v
      i = i.next

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
      print(f'calls={calls} gr={gr} (+{gr1}-{gr2}) dup={dup} maxLen={maxLen} pm_friends={users[pm].count if users[pm] else 0} time={time.perf_counter() - t:0.3f}')
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
      g1 = llist(u1)
      users[u1] = g1
      gr += 1 # stat
      gr1 += 1 # stat
    if g2:
      if g2.count > g1.count:
        g1, g2 = g2, g1
        u1, u2 = u2, u1

      g1.addAll(g2)
      gr2 += 1 # stat
      gr -= 1 # stat
      for u in g2:
        users[u] = g1
    else:
      g1.add(u2)
      users[u2] = g1

    maxLen = max(maxLen, g1.count)
    if g1 == users[pm] and g1.count >= needFriends:
      print(f'PM is a common friend ({g1.count}) after {calls} calls')
      return 

import time
t = time.perf_counter()

calc(524287)

print(f'elapsed_time={time.perf_counter() - t:0.3f}')
