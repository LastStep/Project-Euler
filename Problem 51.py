import time
start = time.time()

def prime(n):
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True

def repeat(n):
    n = [i for i in str(n)[:-1]]
    for i in n:
        if n.count(i) == 3:
            return True, int(i)
    return False, 0

def check(n,num):
    nums = [0,1,2,3,4,5,6,7,8,9]
    count = 1
    for i in nums:
        if i == num:
            continue
        else:
            m = [int(j) if int(j) != num else i for j in str(n)]
            m = int(''.join(str(j) for j in m))
            if len(str(m)) == 6 and prime(m):
                count += 1
    if count == 8:
        return True
    return False
            
def main():
    for i in range(100001,1000000,2):
        test, num = repeat(i)
        if test and prime(i):
            if check(i,num):
                return i

            
print(main())
       
end = time.time()
print(end-start)