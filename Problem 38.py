import time
from itertools import permutations
start = time.time()

def pan(n):
    n = [int(i) for i in str(n)]
    check = [False for i in n if n.count(i) > 1]
    return all(check)
    
def check(n):
    for i in range(1,5):
        temp, j = '', 0
        while len(temp) < 9:
            temp += str(int(n[:i])*num[j])
            j += 1
        if n == temp:
            return True
    return False


num = [i for i in range(1,10)]

def main():
    for i in permutations(num[::-1]):
        i = ''.join(str(j) for j in i)
        if check(i):
            return i

print(main())


end = time.time()
print(end-start)