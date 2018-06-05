ans = []

for i in range(1,2**20):
    b = list(str(bin(i))[2:])
    b = map(int, b)
    bi =  [0]*20
    bi.extend(b)
    bi = bi[-19:]

    n = reduce(lambda a, b: a*b, [x*y for x,y in zip(bi,range(1,20)) if x*y != 0],1)


    if len([a for a in range(1,20) if n%a==0])==19:
        ans.append(n)


print sorted(ans)[0]
