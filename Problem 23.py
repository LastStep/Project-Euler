import time
start = time.time()

def d(n):
    count = 1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            count += i
            j = n//i
            if j>i:
                count += j
    return count

ab = []
n = 28123
for i in range(1,n+1):
    if d(i) > i:
        ab.append(i)

count = sum(range(n+1))
d = {}

for k,i in enumerate(ab):
    for j in ab[k::]:
        if i+j not in d:
            if i + j < n+1:
              d[i+j] = i + j
            else:
                break
      
                
               


print(count - sum(d))

end = time.time()
print(end-start)