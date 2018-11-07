numwords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
numwords10 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
numwords100 = ['hundred']
numwords1000 = ['thousand', 'million', 'billion']
def num2word(n):
  s = []

  def stripOrders(n, p10, wordArr):
    for i in range(len(wordArr), 0, -1):
      t = n // 10**(p10*i)
      if t > 0:
        return (n % 10**(p10*i), num2word(t) + [wordArr[i-1]])
    return (n, [])

  n, s = stripOrders(n, 3, numwords1000)
  if s != []:
    if n > 0:
      s += num2word(n)
    return s
  n, s = stripOrders(n, 2, numwords100)
  if s != []:
    if n > 0:
      s += ['and'] + num2word(n)
    return s

  if n > 0 and n < 20:
    s += [numwords[n]]
    n = 0
  if n >= 20:
    s += [numwords10[n//10 - 2]]
    if n % 10 != 0:
      s += num2word(n % 10)

  if s == []:
    s = [numwords[0]]
  return s

s = 0
for i in range(1, 1001):
  s += len(''.join(num2word(i)))
print(s)
