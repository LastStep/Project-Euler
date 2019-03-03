import time
start = time.time()


def check(n):
    x = (1+(1+24*n)**0.5)/6
    return x == int(x)

def main():
    n = 1
    while True:
        y = 0.5*n*(3*n-1)
        for i in range(n-1,0,-1):
            x = 0.5*i*(3*i-1)
            if check(y-x) and check(y+x):
                return int(y-x)
        n += 1
        
        
print(main())            

                
        
        
        
end = time.time()
print(end-start)