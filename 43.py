s = 0
for d1 in range(1, 10):  
  for d2 in range(0, 10): 
    if d2 not in [d1]:
      for d3 in range(0, 10):
        if d3 not in [d1, d2]:
          for d4 in range(0, 10):
            if d4 not in [d1, d2, d3] and d4 % 2 == 0:
              for d5 in range(0, 10):
                if d5 not in [d1, d2, d3, d4] and (d3 + d4 + d5) % 3 == 0:
                  for d6 in range(0, 10):
                    if d6 not in [d1, d2, d3, d4, d5] and d6 in [0, 5]:
                      for d7 in range(0, 10):
                        if d7 not in [d1, d2, d3, d4, d5, d6] and (d5 * 100 + d6*10 + d7) % 7 == 0:
                          for d8 in range(0, 10):
                            if d8 not in [d1, d2, d3, d4, d5, d6, d7] and (d6 * 100 + d7*10 + d8) % 11 == 0:
                              for d9 in range(0, 10):
                                if d9 not in [d1, d2, d3, d4, d5, d6, d7, d8] and (d7 * 100 + d8*10 + d9) % 13 == 0:
                                  for d10 in range(0, 10):
                                    if d10 not in [d1, d2, d3, d4, d5, d6, d7, d8, d9] and (d8 * 100 + d9*10 + d10) % 17 == 0:
                                      n = d1*10**9+d2*10**8+d3*10**7+d4*10**6+d5*10**5+d6*10**4+d7*1000+d8*100+d9*10+d10
                                      print(n)
                                      s += n

print(s)
