import time
from fractions import Fraction
start = time.time()


def iterations(n, x = 2):
    if n == 1:
        num = str(Fraction(1+1/x))
        num = num.split('/')
        if len(num[0]) > len(num[1]):
            return True
        return False
    else:
        n -= 1
        x = Fraction(2 + 1/x)
        return iterations(n, x)

 
def main():
    count = 0
    for i in range(1,1001):
        if iterations(i):
            count += 1
    return count

print(main())       



       
end = time.time()
print(end-start)