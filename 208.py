steps = [ # 5 'orthogonal' directions (with prime numbers as coords and 0 in total)
  (1, 11),
  (2, -1),
  (3, -2),
  (-1,-3),
  (-5,-5),
]

def stepNturn(p, direction):
  return (p[0] + steps[p[2]][0], p[1] + steps[p[2]][1], (p[2] + direction) % 5)

mem = {}
def walk(p, n, log = []):
  if n == 0:
    return 1 if p[2] == 0 else 0

  if not log:
    log = [n // 5] * 5
  log[p[2]] -= 1
  if log[p[2]] < 0:
    return 0

  s = str(n)+':'+str(p)
  if s in mem:
    return mem[s]

  res = sum([walk(stepNturn(p, d), n - 1, log[::]) for d in [1, -1]])
  mem[s] = res
  return res

print(walk((0, 0, 0), 70))
