import time
start = time.time()


def spiral(n):
    level, layer, temp , check, res = 1, 1, 0, 0, 0
    limit = (n + 1)/2
    while check < limit:
        for i in range(temp, level**2 + 1, layer):
            res += i
        res -= temp
        check += 1
        temp = level**2
        level = 2*check + 1
        layer = 2*check
    return res

print(spiral(1001))

end = time.time()
print(end-start)


