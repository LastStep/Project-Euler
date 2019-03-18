import time

t1 = time.time()

def sumprime(x):
    summ, s = [2], [True]*x
    for i in range(3, x, 2):
        if s[i]:
            summ.append(i)
            for j in range(i*i, x, i):
                s[j] = False
    return summ   
	

print(sum(sumprime(2000000)))



t2 = time.time()
print(t2-t1)	
