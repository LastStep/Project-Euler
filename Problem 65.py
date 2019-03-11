import time
start = time.time()

def e_series(n):
	s = [int(2*(i/3 + 1)) if i%3 == 0 else 1 for i in range(n-2)]
	s.insert(0,1)
	s.insert(0,2)
	return s
	
	
def fraction(s):
	num, den = 1, 0
	for i in reversed(s):
		num, den = num*i + den , num
#		print('{0}/{1}'.format(num,den))
	res = 0
	for i in str(num):
		res += int(i)
	return res
	
def main(n):
	return fraction(e_series(n))

print(main(100))

end = time.time()
print(end-start)