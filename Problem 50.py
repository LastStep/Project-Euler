import time
start = time.time()

def sieve(n):
    prime = [True]*(n+1)
    prime[0] = False
    prime[1] = False
    i = 2
    p = []
    while i <= n:
        if prime[i]:
            p.append(i)
            for j in range(2*i, n+1, i):
                prime[j] = False
        i += 1
    return p
     
prime = sieve(5000)

def p(n):
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True

def main(m):
    n, res = 0, [0,0]
    while sum(prime[:n]) < m:
        length = n
        n += 1
    for i in range(length+1)[::-1]:
        for j in range(i):
            if res[0] < i-j:
                if p(sum(prime[j:i])):
                    res[0] = i-j
                    res[1] = sum(prime[j:i])
            else:
                break
                
    return res, length

print(main(1000000))



        
end = time.time()
print(end-start)