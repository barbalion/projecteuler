steps = [ # 5 directions (with prime numbers as coords and 0 in total)
  (0, 11),
  (-3, -1),
  (-2, -2),
  (2, -3),
  (3, -5),
]

def stepNturn(p, direction):
  return (p[0] + steps[p[2]][0], p[1] + steps[p[2]][1], (p[2] + direction) % 5)

mem = {}
def walk(p, n):
  if n == 0:
    return 1 if p[0] == 0 and p[1] == 0 and p[2] == 0 else 0

  s = str(n)+':'+str(p)
  if s in mem:
    return mem[s]

  res = walk(stepNturn(p, 1), n - 1) + walk(stepNturn(p, -1), n - 1)
  mem[s] = res
  return res

print(walk((0, 0, 0), 70))
