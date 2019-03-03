import time
start = time.time()


def d(n):
    count = 1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            count += i
            j = n//i
            if j>i:
                count += j
    return count

count = 0
for i in range(1,10000):
    j = d(i)
    if i == d(j) and i != j:
        count += i
        
print(count)

end = time.time()
print(end-start)