import inflect
p = inflect.engine()
s = []

for i in range(1,1001):
    s.append(p.number_to_words(i).replace(" ","").replace("-",""))


import re

print len("".join(s))
