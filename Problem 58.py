import time
start = time.time()

def prime(n):
    if n%2 == 0 or n == 1:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n%i == 0:
            return False
    return True


def spiral(n):
    level, layer, temp , check, res = 1, 1, 1, 0, [0,-3]
    limit = 100
    while limit > 10:
        for i in range(temp, level**2 + 1, layer):
            if prime(i):
                res[0] += 1
        res[1] += 4
        check += 1
        temp = level**2
        level = 2*check + 1
        layer = 2*check
        if check > 1:
            limit = 100*(res[0]/res[1])
    
    return 2*(check-1) + 1

print(spiral(4))

end = time.time()
print(end-start)


