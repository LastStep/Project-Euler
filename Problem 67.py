import time
import numpy as np
start = time.time()  

f = open(r'C:\Users\Gray\Documents\Python Scripts\p067_triangle.txt')

d ={}

for k,i in enumerate(f.readlines()):
	i = i.split()
	i = [int(j) for j in i]
	d[k] = np.array(i)
	n = k

f.close()
	
n = [i for i in range(n,0,-1)]
	
for i in n:
	d[i-1] += np.array([max(d[i][k],d[i][k+1]) for k in range(len(d[i])-1)])
	
print(d[0])

end = time.time()
print(end-start)
