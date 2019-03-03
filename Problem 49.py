import time
start = time.time()

def sieve(n):
    prime = [True]*(n+1)
    prime[0] = False
    prime[1] = False
    i = 2
    while i*i <= n:
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
        i += 1
    return prime
     
prime = sieve(10000)
d = {}    
def perm(n):
    i = 2
    while n+i+i < 10000:
        if prime[n+i] and prime[n+i+i]:
            if set(str(n)) == set(str(n+i)) == set(str(n+i+i)):
                d[n] = (n+i,n+i+i)
                return True
        i += 2
    return False   


def main():
    for i in range(1000,10000):
        if prime[i] and perm(i):
            continue
    return d


print(main())        
    




        
end = time.time()
print(end-start)