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
	temp = []
	for k,j in enumerate(d[i]):
		if k < len(d[i]) - 1: temp.append(max(d[i][k],d[i][k+1]))
	d[i-1] = d[i-1] + np.array(temp)

print(d[0])

end = time.time()
print(end-start)
