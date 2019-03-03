import time

start = time.time()

def prime(n):
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True
   
def int2list(n):
    m = str(n)
    m = [int(i) for i in m]
    return m
def list2int(n):
    m = int(''.join(str(i) for i in n))
    return m
def check(n):
    n = int2list(n)
    for i in n:
        if i%2 == 0 or i%5 == 0:
            return True
    return False
    
def cy(n):
    n = int2list(n)   
    for i in range(len(n)-1):
        index = 0
        while index < len(n) - 1:
            temp = n[index]
            n[index] = n[index+1]
            n[index+1] = temp
            index += 1
        m = list2int(n)
        if m not in d and prime(m):
            d[m] = 1
        else:
            return False
    return True

count, d = 1, {2:1}

for i in range(3,1000000,2):
    if check(i):
        continue
    if prime(i):
        if i not in d and cy(i):
            count += len(str(i))

print(count)

end = time.time()
print(end-start)