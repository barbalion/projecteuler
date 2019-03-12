import numpy
S = [0] * 300001

def fillLagFib():
  for k in range(1, 56):
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

def minmax(cubes, coord):
  return range(min([c[coord] for c in cubes]), max([c[coord]+c[coord+3] for c in cubes]))

def subcubes(cubes, x, coord): 
  return [c for c in cubes if x >= c[coord] and x < c[coord] + c[coord+3]]

fillLagFib()

m = 1
size = 10000 + 399 + 1
vol = [[[[0] for i in range(size)] for j in range(size)] for k in range(size)]
cubes = [cube(n) for n in range(1, m + 1)]
v = 0
t = 0

for x in minmax(cubes, 0):
  xcubes = subcubes(cubes, x, 0)
  #print(x, xcubes)
  if xcubes:
    for y in minmax(xcubes, 1):
      ycubes = subcubes(xcubes, y, 1)
      #print(x, y, ycubes)
      if ycubes:
        for x0, y0, z0, dx, dy, dz in ycubes:
          for z in range(z0, z0 + dz):
            if not (x >= x0 and x < x0+dx and y >= y0 and y < y0+dy):
              continue
            nu = dz + z0 - z 
            t += 1
            if vol[x][y][z] >= nu:
              t += nu
              break
            if not vol[x][y][z]:
              v += 1
            vol[x][y][z] = nu
print(v, t)
print(sum([dx * dy *dz for x0, y0, z0, dx, dy, dz in ycubes]))