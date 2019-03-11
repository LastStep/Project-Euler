import time
start = time.time()

d = {}
res = {}

def main(x):
	n = 1
	while True:
		cube = str(n**3)
		m = [i for i in cube]
		m.sort()
		m = ''.join(m)
		if m in d.values():
			k = list(d.keys())[list(d.values()).index(m)]
			res[k] += 1
			if res[k] == x:
				return k
		else:
			d[int(cube)] = m
			res[int(cube)] = 1
		n += 1
		
print(main(5))

end = time.time()
print(end-start)