f = open("p042_words.txt").read().replace("\"","").split(",")



f = map(lambda a: sum(map(lambda b: ord(b)-64, a)), f)




triangles = [1]
i = 1
while triangles[-1] < max(f):
     i+= 1
     triangles.append(0.5*i*(i+1))

print len(filter(lambda a: a in triangles, f))
