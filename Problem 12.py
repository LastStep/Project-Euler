import time
t1 = time.time()

def factors(n):
    d = {}
    count = 1
    while n%2 == 0:
        n /= 2
        try:
            d[2] += 1
        except KeyError:
            d[2] = 1
    for i in range(3, int((n+1)**0.5)+1, 2):
        while n%i == 0 and n != i:
            n /=  i
            try:
                d[i] += 1
            except KeyError:
                d[i] = 1
    d[n] = 1
    for key,value in d.items():
        count = count*(value+1)
    return count        

def triangle(n):
    z, i = 0, 1
    while z < n:
        z = factors(i*(i+1)/2)
        i += 1
    print(sum(range(i)))
        
triangle(500)

t2 = time.time()
print(t2-t1)	
