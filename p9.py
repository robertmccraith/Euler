print [(a,b,c) for a in range(1,999) for b in range(a,999) for c in range(b, 999) if (a**2 + b**2 == c**2) and a+b+c==1000][0]
