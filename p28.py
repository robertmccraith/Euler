x = range(1,1002, 2)
i = 2

corners = []
for i in range(1, len(x)):
    corners.extend(range(x[i-1]**2, x[i]**2, i*2))

print sum(corners)+x[-1]**2
