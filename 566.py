from tools import *

def debug(str):
  print(str)
  pass

class MyNum:
  def __init__(self, n, d, k, c, renorm = True):
    if renorm:
      cq = int(c**.5)
      if cq*cq == c:
        n, d, k = k*d+n*cq, d*cq, 0
      cd = gcd(n, d)
      self.n = n // cd
      self.d = d // cd
    else:
      self.n = n
      self.d = d
    self.k = k
    self.c = c
    self.val = self.eval()

  def add(self, that):
    return MyNum(self.n*that.d + that.n*self.d, that.d*self.d, self.k+that.k, self.c)
  def sub(self, that):
    return MyNum(self.n*that.d - that.n*self.d, that.d*self.d, self.k-that.k, self.c)

  def eval(self):
    return self.n/self.d + self.k/(self.c**.5)

  def __gt__(self, other):
    return self.val > other.val #and not self.__eq__(other)
  def __lt__(self, other):
    return self.val < other.val #and not self.__eq__(other)
  def __eq__(self, other):
    return self.n==other.n and self.d==other.d and self.c==other.c and self.k==other.k
    #debug('================', self.val, other.val, abs(self.val-other.val))
    #return abs(self.val-other.val)<1e-4
    #return self.val==other.val
  def __str__(self):
    return f'{self.val*10:0.0f}'
    #return f'{self.val}={(self.n, self.d, self.k, self.c)}'
  def __repr__(self):
    return self.__str__()
  def __ne__(self, other):
    return not self.__eq__(other)
class Slice:
  lastId=0

  def __init__(self, size, state=1):
    self.size = size
    self.state = state
    self.prev = self
    self.next = self
#    Slice.lastId += 1
#    self.id = Slice.lastId
    self._recurReenter = False

  def __str__(self):
    if self._recurReenter:
      return ''
    self._recurReenter = True
    try:
      #return f'({int(self.size.val*self.state)})---{self.next}' 
      return f'({self.size})---{self.next}' 
    finally:
      self._recurReenter = False
  def __repr__(self):
    return self.__str__()

  def sumSize(self):
    if self._recurReenter:
      return (0, MyNum(0, 1, 0, 1))
    self._recurReenter = True
    try:
      l, s = self.next.sumSize()
      return (l + 1, self.size.add(s))
    finally:
      self._recurReenter = False

  def cut(self, s):
#    if s > self.size:
#      raise Excestion(f'cut {s} > {self.size}')
    if s == self.size:
#      debug('  no cutting!')
      return self
#    debug(f'  cut {s}, {self}')
    new = Slice(self.size.sub(s), self.state)
    new.add(self)
    self.size = s
#    debug(f'    cut done {self}')
    return new

  def cutNClue(self, s):
    p = self.prev
    if self.state == p.state:
      raise Exception(f'can\'t cut-n-clue: {self}')
    p.size = p.size.add(s)
    if s == self.size:
      self.remove()
    else:
      self.size = self.size.sub(s)
    return p

  def isOne(self):
    return self.next == self  

  def clue(self):
    if self.isOne():
      return self
    p = self.prev
    if p.state == self.state:
#      debug(f'  clue {self.size}, {self.next.size}')
      p.size = p.size.add(self.size)
      self.remove()
#      debug(f'    clued {self}')
      return p
    return self

  def remove(self):
    self.prev.next, self.next.prev, self.next, self.prev = self.next, self.prev, self, self

  def add(self, after):
    self.prev, self.next, after.next.prev, after.next = after, after.next, self, self

  def move(self, after):
    self.remove()
    self.add(after)

  def exchange(self, other):
    p = self.prev
    self.move(other)
    other.move(p)
    #self.prev, self.next, other.prev, other.next, self.prev.next, self.next.prev, other.prev.next, other.next.prev = other.prev, other.next, self.prev, self.next, other, other, self, self

  def flip(self, other):
#    debug(f'  flip {self.id}, {other.id}: {self}')
    self.state = -self.state
    if self == other:
#      debug(f'    flipped one: {self}')
      return
    other.state = -other.state
    self.exchange(other)
#    debug(f'    flipped: {other}')
    if other.next != self:
#      debug(f'    flipping more...')
      other.next.flip(self.prev)

def calc(a, b, c):
  r = 360
  def stepGen():
    while True:
      yield MyNum(r, a, 0, c)
      yield MyNum(r, b, 0, c)
      yield MyNum(0, 1, 360, c)

#      yield MyNum(0, 1, 360, 10)
#      yield MyNum(360, 2, 0, 1)
#      yield MyNum(360, 3, 0, 1)
#      yield MyNum(360, 17, 0, 1)


  pie = Slice(MyNum(r, 1, 0, c))
  n = 0
  for st in stepGen():
    n += 1
    p = pie
#    debug(f'step{n}: st={st}, pie={pie}')
    while st > pie.size:
      st = st.sub(pie.size)
      pie = pie.next
#      debug(f'  skipped slice: st={st}, pie={pie}, p={p}')
    if p == pie and pie.state != pie.prev.state:
      pie = pie.cutNClue(st).next
    else:
      pie.cut(st)
      p.flip(pie)
      p, pie = pie, p.next
      p.clue()
    #debug(f'  step done[{n}]: sum={pie.sumSize()} {pie}')

    if n % 10000 == 0:
      print(n, pie.sumSize(), pie, flush=True)
    if pie.isOne() and pie.state==1:
      return n


#print(calc(9, 10, 11)) #60
#print(calc(10, 14, 16)) #506
print(calc(11, 13, 15)) #67704
#print(calc(15, 16, 17)) # 
#print(calc(9, 10, 28)) # forever
elapsed()
exit()

#N = 30

#for a in range(2, N+1):
#  for b in range(a+1, N+1):
#    print(a, b, calc(a, b, 1))
#elapsed()
#exit()

#for c in range(2, 200):
#   print(c, calc(9, 10, c))
#exit()

N = 30
s = 0
for a in range(9, N+1):
  for b in range(a+1, N+1):
    for c in range(b+1, N+1):
      res = calc(a, b, c)
      s += res
      print(a, b, c, res, s, flush=True)

print(s)

elapsed()