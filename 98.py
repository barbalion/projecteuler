from itertools import groupby

def readWords():
  with open("p098_words.txt", "r") as f:
    return f.read().replace('"', '').split(",")

def signature(w):
  chars = {}
  for l in str(w):
    if not l in chars:
      chars[l] = 0
    chars[l] += 1 
  return ''.join(sorted([str(n) for (l,n) in chars.items()]))

def squareMap(maxNum):
  squares = {}
  for sq in [a*a for a in range(1, 10**((maxNum+1)//2))]:
    k = signature(sq)
    if k not in squares:
      squares[k] = set()
    squares[k].add(sq)
  return squares

def trace(w):
  return ''.join(sorted(w))

def annagrams(words):
  tr=lambda w: trace(w)
  return list(filter(lambda ws: len(ws)>1, list([list(ws) for (k, ws) in groupby(sorted(words, key=tr), tr)])))
  # a human-friendly equivalent code follows
  traces = {}
  anns = []
  for w in words:
    tr = trace(w)
    if tr in traces:
      traces[tr] += [w]
    else:
      traces[tr] = [w]
  return list(filter(lambda ws: len(ws)>1, traces.values()))

def remapLetterToNums(w1, w2, a):
  for l, n in zip(w1, str(a)):
    w2 = w2.replace(l, n)
  return int(w2)

words = readWords()
anns = annagrams(words)
pairs=sum([[(w1, w2) for w1 in ws for w2 in ws if w1 > w2] for ws in anns], [])

maxLen = max([max(arr) for arr in [[len(w) for w in ws] for ws in anns]])
squares = squareMap(maxLen)

m = 0
for w1, w2 in pairs:
  #print(w1, w2)
  sig = signature(w1)
  nums = squares[sig]
  for a in nums:
    if remapLetterToNums(w1, w2, a) in nums:
      m = max(m, a, remapLetterToNums(w1, w2, a))
      print(w1, w2, a, remapLetterToNums(w1, w2, a), m)
