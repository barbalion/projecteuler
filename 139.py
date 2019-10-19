from tools import *
import sys

# walk Primitive Pythagorean triples
sys.setrecursionlimit(10000)
def walkTriples(a, b, c, M, f):
  s = a + b + c
  if (s >= M):
    return
  f(a, b, c, s)
  for a, b, c in [
      (a-2*b+2*c, 2*a-b+2*c, 2*a-2*b+3*c),
      (a+2*b+2*c, 2*a+b+2*c, 2*a+2*b+3*c),
      (-a+2*b+2*c, -2*a+b+2*c, -2*a+2*b+3*c)]:
    walkTriples(a, b, c, M, f)

M = 10**8
cnt = 0
def check(a, b, c, s):
  global cnt
  if c % (b-a) == 0:
    #print(a, b, c, s, (c*c), (2*a*b), M // s)
    cnt += (M-1) // s

walkTriples(3, 4, 5, M, check) 

print(cnt)

elapsed()
