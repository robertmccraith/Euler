def pandigital(s):
    return len(s) == 9 and len(set(s)) == 9 and '0' not in s


l = 0

for i in range(2, 10000):
    for j in range(2, 9):
        x = reduce(lambda a,b: a+str(i*b),range(1,j+1),"" )

        if pandigital(x) and l < x:
            l = x
            print x
