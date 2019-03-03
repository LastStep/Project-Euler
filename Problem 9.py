import time

t1 = time.time()

for a in range(1,1000):
    for b in range(a+1,1000-2*a):
        c = 1000 - a - b
        if a+b+c == 1000:
            if a**2 + b**2 == c**2:
                print(a*b*c)
                break

t2 = time.time()
print(t2-t1)