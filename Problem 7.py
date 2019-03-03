import time

t1 = time.time()

def prime(x):
	for i in range(3, int(x**0.5)+1, 2):
		if x%i == 0:
			return False
	return True

n = 2
x = 3
while n<10001:
	x += 2
	if prime(x):
		n += 1
	

t2 = time.time()
print(x, t2-t1)
	
