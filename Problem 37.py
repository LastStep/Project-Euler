import time

start = time.time()

def prime(n):
    if n == 1:
        return False
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5) + 1, 2):
        if n%i == 0:
            return False
    return True

def int2list(n):
    m = str(n)
    m = [int(i) for i in m]
    return m

def trunc(n):
    n = str(n)
    for i in range(len(n)-1):
        if not prime(int(n[:-i-1])):
            return False
        if not prime(int(n[i+1:])):
            return False
    return True

def p_list(a,b):
    while len(p) != 11:
        for i in [a,b]:
            check = True
            m = int2list(i)
            if m[-1] == m[-2] or m[0] == m[1]:
                continue
            for j in m:
                if j%2 == 0:
                    check = False
                    break
            if check and prime(i) and trunc(i):
                p.append(i)
        a += 20
        b += 20
    return 

p = [23]
p_list(13,17)
p.sort()
print(p,len(p),sum(p))


end = time.time()
print(end-start)