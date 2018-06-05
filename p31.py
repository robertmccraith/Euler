s = 2 # all 1p and one 2 pound

for a in range(0,2):# 100p
    for b in range(0,5): # 50p
        for c in range(0,11): # 20p
            for d in range(0, 21): # 10p
                for e in range(0, 41): # 5p
                    for f in range(0, 101): # 2p
                        total = 100*a + 50*b + 20*c + 10*d + 5*e + 2*f
                        if total > 200:
                            break
                        s+=1
print s
