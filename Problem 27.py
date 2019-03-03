import time
start = time.time()

def prime(n):
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def func(a, b):
    check, n = 1, 1
    num = n*(n+a) + b
    while prime(num):
        check += 1
        n += 1
        num = n*(n+a) + b
        if num < 0:
            break
    return check - 1

res, b = [0, 0, 0], []
for i in range(2,1000):
    if prime(i):
        b.append(i)
        
for i in range(-999,1000,2):
    for j in b:
        if abs(i) <= j:
            seq = func(i, j)
            if seq > res[0]:
                res[0] = seq
                res[1] = i
                res[2] = j
                
print(res, res[1]*res[2])
            




end = time.time()
print(end-start)


