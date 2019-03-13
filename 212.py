def genBoxes(m):
  S = [0] * (m * 6 + 1)

  def fillLagFib():
    for k in range(1, min(56, len(S))):
      n = (100003 - 200003 * k + 300007 * k**3) % 1000000
      S[k] = n
    for k in range(56, len(S)):
      n = (S[k-24] + S[k-55]) % 1000000
      S[k] = n

  def cube(n):
    return (
      S[6*n-5] % 10000,   # x0
      S[6*n-4] % 10000,   # y0
      S[6*n-3] % 10000,   # z0
      1 + S[6*n-2] % 399, # dx
      1 + S[6*n-1] % 399, # dy
      1 + S[6*n-0] % 399, # dz
    )

  def box(c):
    x0, y0, z0, dx, dy, dz = c
    return (x0, y0, z0, x0 + dx, y0 + dy, z0 + dz)

  fillLagFib()
  return [box(cube(n)) for n in range(1, m + 1)]

def intersect(a, b):
  ax1, ay1, az1, ax2, ay2, az2 = a
  bx1, by1, bz1, bx2, by2, bz2 = b
  return [(x1, y1, z1, x2, y2, z2) for x1, y1, z1, x2, y2, z2 in [
    (max(ax1, bx1), max(ay1, by1), max(az1, bz1), min(ax2, bx2), min(ay2, by2), min(az2, bz2))
  ] if x2 > x1 and y2 > y1 and z2 > z1]

def vol(box):
  x1, y1, z1, x2, y2, z2 = box
  return (x2-x1) * (y2-y1) * (z2-z1) 

def getVolOfCell(c, boxes, dep=0):
  v = vol(c)
  iv = 0
  subbox = []
  for b in boxes:
    for i in intersect(c, b):  
      if vol(i) == v:
        #print(c, boxes, v)
        return v
      iv = vol(i)
      subbox.append(b)
  if not subbox:
    return 0
  if len(subbox) == 1:
    return iv
  if len(subbox) == 2:
    i1, i2 = sum([intersect(c, b) for b in subbox], [])
    return vol(i1) + vol(i2) - sum([vol(b) for b in intersect(i1, i2)])
  x1, y1, z1, x2, y2, z2 = c
  mx = (x2-x1)//2 + x1
  my = (y2-y1)//2 + y1
  mz = (z2-z1)//2 + z1
  return sum([getVolOfCell(c2, subbox, dep+1) for c2 in [
    (x1, y1, z1, mx, my, mz), 
    (mx, y1, z1, x2, my, mz), 
    (mx, my, z1, x2, y2, mz), 
    (mx, my, mz, x2, y2, z2), 
    (x1, my, z1, mx, y2, mz), 
    (x1, my, mz, mx, y2, z2), 
    (x1, y1, mz, mx, my, z2), 
    (mx, y1, mz, x2, my, z2), 
  ]])

import time
t = time.perf_counter()

print(getVolOfCell((0, 0, 0, 16384, 16384, 16384), genBoxes(50000)))

print(f'elapsed_time={time.perf_counter() - t:0.3f}')
