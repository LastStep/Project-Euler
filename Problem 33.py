import time
from fractions import Fraction

start = time.time()

def int2list(n):
    n = str(n)
    n = [int(i) for i in n]
    return n
def list2int(n):
    n = int(''.join(str(i) for i in n))
    return n

def fraction(a, b):
    a, b = int2list(a), int2list(b)
    d = {}
    for i in a:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    c = [] + b
    check = False
    for k,i in enumerate(b):
        if i in d and d[i] != 0:
            a.remove(i)
            c.remove(i)
            d[i] -= 1  
            check = True
    if len(a) == 0:
        a, check = [0], False
    if len(c) == 0:
        c, check = [0], False
    
    d.clear()
    return list2int(a), list2int(c), check

res = [1,1]

for i in range(10, 99):
    if i%10 != 0:
        for j in range(i+1, 100):
            a, b, check = fraction(i, j)
            if check:
                try:
                    if float(a/b) == float(i/j):
                        print(i,j)
                        res[0] *= a
                        res[1] *= b
                except ZeroDivisionError:
                    continue
                
print(Fraction(res[0],res[1]))        




end = time.time()
print(end-start)