marked = [0]*2000000

n = 3

csum = 2

while n < 2000000:
    if marked[n] == 0:
        csum += n
        i = n
        while i < 2000000:
            marked[i] = 1
            i += n
    n += 2
print csum
