import time
import numpy as np
from itertools import permutations
start = time.time()

def num(n):
	return n%100*100

tri = [int(0.5*n*(n+1)) for n in range(150) if 999 < int(0.5*n*(n+1)) < 10000]
sq = [n*n for n in range(150) if 999 < n*n < 10000]
penta = [int(0.5*n*(3*n-1)) for n in range(150) if 999 < int(0.5*n*(3*n-1)) < 10000]
hexa = [n*(2*n-1) for n in range(150) if 999 < n*(2*n-1) < 10000]
hepta = [int(0.5*n*(5*n-3)) for n in range(150) if 999 < int(0.5*n*(5*n-3)) < 10000]
octa = [n*(3*n-2) for n in range(150) if 999 < n*(3*n-2) < 10000]

arr = np.array([np.array(tri),np.array(sq),np.array(penta),np.array(hexa),np.array(hepta)])

res = []

def test(narr, x, n, m):
	index = np.where(narr[n] < x, 0, np.where(narr[n] > x+100, 0, narr[n]))
	index = np.nonzero(index)
	for i in narr[n][index]:
		res.append(i)
		if n == 4:
			if str(i)[2:] == str(m)[:2]:
				return True
			return False
		elif test(narr, num(i), n+1, m):
			return True
		else:
			continue
	return False
		
		 
def main():
	narr = np.copy(arr)
	for k in permutations([0,1,2,3,4]):
		for i in octa:
			if test(narr,num(i), 0, i):
				res.insert(0,i)
				break
			res.clear()
		if len(res) == 0:
			narr = np.copy(arr[[*k]])
		else:
			return res, sum(res)
	
	
print(main())
 
end = time.time()
print(end-start)
