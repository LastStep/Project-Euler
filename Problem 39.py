import time
start = time.time()


res = [0,0]
p = 2
while p <= 1000:
    count = 0
    for a in range(1,int(p/3)):
        b = (p*(p-2*a))/(2*(p-a))
        if a < b and (p*(p-2*a)) % (2*(p-a)) == 0:
            count += 1
    if count > res[0]:
        res[0] = count
        res[1] = p
    p += 2
    
print(res)


end = time.time()
print(end-start)