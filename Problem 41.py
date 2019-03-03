import time
from itertools import permutations
start = time.time()


def prime(n):
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True


def main():
    num = [i for i in range(1,10)]
    while True:
        if sum(num)%3 != 0:
            for i in permutations(num[::-1]):
                i = ''.join(str(j) for j in i)
                if prime(int(i)):
                    return i
        num = num[:-1]

print(main())


end = time.time()
print(end-start)