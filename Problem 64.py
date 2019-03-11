import time
start = time.time()


def ContinuedFraction(n):
	m = 0
	d = 1
	a0 = int(n**0.5)
	M = d*a0-m
	D = (n-M**2)/d
	A = int((a0+M)/D)
	i = 2
	check = (M,D,A)
	while True:
		m = D*A-M
		d = (n-m**2)/D
		a = int((a0+m)/d)
		if check == (m,d,a):
			return i%2 == 0
		M, D, A = m, d, a
		i += 1
			
def main(N):
	count = 0
	for i in range(2,N+1):
		if i**0.5 != int(i**0.5):
			if ContinuedFraction(i):
				count += 1
	return count

print(main(10000))

end = time.time()
print(end-start)