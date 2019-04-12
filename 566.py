from tools import *

def debug(*str):
  #print(*str)
  pass

class MyNum:
  def __init__(self, n, d, k, c):
    cq = int(c**.5)
    if cq**2 == c:
      n, d, k, c = k*d+n*cq, d*cq, 0, 1
    cd = gcd(n, d)
    self.n = n // cd
    self.d = d // cd
    self.k = k
    self.c = c

  def add(self, that):
    return MyNum(self.n*that.d + that.n*self.d, that.d*self.d, self.k+that.k, self.c)
  def sub(self, that):
    return MyNum(self.n*that.d - that.n*self.d, that.d*self.d, self.k-that.k, self.c)

  def eval(self):
    return self.n/self.d + self.k/(self.c**.5)

  def __gt__(self, other):
    return self.eval() > other.eval() #and not self.__eq__(other)
  def __lt__(self, other):
    return self.eval() < other.eval() #and not self.__eq__(other)
  def __eq__(self, other):
    return self.n==other.n and self.d==other.d and self.c==other.c and self.k==other.k
    #debug('================', self.eval(), other.eval(), abs(self.eval()-other.eval()))
    #return abs(self.eval()-other.eval())<1e-4
    #return self.eval()==other.eval()
  def __str__(self):
    return str(int(self.eval()))
    #return f'{self.eval()}={(self.n, self.d, self.k, self.c)}'
  def __ne__(self, other):
    return not self.__eq__(other)
class Slice:
  lastId=0

  def __init__(self, size, state=1):
    self.size = size
    self.state = state
    self.prev = self
    self.next = self
    Slice.lastId += 1
    self.id = Slice.lastId
    self._recurReenter = False

  def __str__(self):
    if self._recurReenter:
      return ''
    self._recurReenter = True
    try:
      return f'({self.size.eval()*self.state})------{self.next}' 
      #return f'({self.id}::{self.size},{self.state})<->{self.next}' 
    finally:
      self._recurReenter = False

  def sumSize(self):
    if self._recurReenter:
      return MyNum(0, 1, 0, 1)
    self._recurReenter = True
    try:
      return self.size.add(self.next.sumSize())
    finally:
      self._recurReenter = False

  def cut(self, p):
#    if p > self.size:
#      raise Exception(f'cut {p} > {self.size}')
    if p == self.size:
#      debug('  no cutting!')
      return self
#    debug(f'  cut {p}, {self}')
    new = Slice(self.size.sub(p), self.state)
    new.add(self)
    self.size = p
#    debug(f'    cut done {self}')
    return new

  def isOne(self):
    return self.next == self  

  def clue(self):
    if self.isOne():
      return self
    p = self.prev
    if p.state == self.state:
#      debug(f'  clue {self.size}, {self.next.size}')
      p.size = self.size.add(p.size)
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
  def stepGen():
    while True:
      yield MyNum(360, a, 0, c)
      yield MyNum(360, b, 0, c)
      yield MyNum(0, 1, 360, c)

#      yield MyNum(0, 1, 360, 10)
#      yield MyNum(360, 2, 0, 1)
#      yield MyNum(360, 3, 0, 1)
#      yield MyNum(360, 17, 0, 1)


  pie = Slice(MyNum(360, 1, 0, c))
  n = 0
  for st in stepGen():
    n += 1
    p = pie
#    debug(f'step{n}: st={st}, pie={pie}')
    while st > pie.size:
      st = st.sub(pie.size)
      pie = pie.next
#      debug(f'  skipped slice: st={st}, pie={pie}, p={p}')
    pie.cut(st)
    p.flip(pie)
    p, pie = pie, p.next
    p.clue()
#    debug('  step done:', pie, 'sum=', pie.sumSize())

#    if n % 1000 == 1:
#      print(n, pie)
    if pie.isOne() and pie.state == 1:
      return n


#print(calc(9, 10, 19))

N = 14
s = 0
for a in range(9, N+1):
  for b in range(a+1, N+1):
    for c in range(b+1, N+1):
      res = calc(a, b, c)
      s += res
      print(a, b, c, res, s)

print(s)

elapsed()