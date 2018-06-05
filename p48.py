s = 0

for i in range(1, 1000):
    s = (s+i**i) % 10000000000
print s
