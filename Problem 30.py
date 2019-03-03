import time

from itertools import combinations_with_replacement

t1 = time.time()
ex, s = 5, 0
p = {str(i):i**int(ex) for i in range(10)}

for cx in combinations_with_replacement('0123456789', int(ex)+(int(ex)>=5)):
    t = sum(p[x] for x in cx)
    sd = sum(p[x] for x in str(t))
    if t==sd and t>9: s+= t

print("Sum of power digits for exponent", ex, "is", (s if s>0 else "*NONE*"))

t2 = time.time()

print(t2-t1)