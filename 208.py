from decimal import *
import time
t = time.perf_counter()

err = 1e-5

def left(v):
  x, y = v
  return (x * c - y * s, y * c + x * s)

def right(v):
  x, y = v
  return (x * c + y * s, y * c - x * s)

def add(v1, v2):
  return (v1[0] + v2[0], v1[1] + v2[1])

def llen(v):
  return v[0] ** 2 + v[1] ** 2

s = (5 / 8 + (5 ** .5) / 8) ** .5
c = (5 ** .5 - 1) / 4

mem = {}

def walk(p, v, n, dep=0):
  if n == 0:
    return 1 if llen(p) < err and abs(v[0]) < err else 0

  global hits, miss, t
  s = str(n)+':'+str(p[0])[:8] + str(p[1])[:8] + str(v[0])[:3] + str(v[1])[:3]
  if s in mem:
    return mem[s]

  p = add(p, v)
  res = walk(p, left(v), n - 1, dep+1) + walk(p, right(v), n - 1, dep+1)
  mem[s] = res
  return res

print(walk((0, 0), (0, 1), 70))
