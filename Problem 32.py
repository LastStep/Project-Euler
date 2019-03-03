import time
from functools import reduce
start = time.time()

def factors(n):    
    return sorted(list(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    
def check(num):
    d = {}
    for l in num:
        if l not in d and int(l) != 0:
            d[l] = 1
        else:
            d = {}
            break
    if len(d) == len(num):
        return True
    return False

def product(n):
    m = factors(n)
    m = m[1:-1]
    p = m[::-1]
    for k,i in enumerate(m):
        for j in p[:-(1+k)]:
            num = i*j
            if num == n and len(str(i) + str(j)) == 5:
                num = str(i) + str(j) + str(n)
                if check(num):
                    return True           
    return False


res = 0

for i in range(1000,10000):
    if check(str(i)) and product(i):
        res += i

print(res)





end = time.time()
print(end-start)