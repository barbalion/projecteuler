lim=100
print((lim*(lim+1)//2)**2 - sum([i * i for i in range(1, lim+1)]))
