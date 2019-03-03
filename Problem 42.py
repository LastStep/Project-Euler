import time, string 
start = time.time()

d = {v:k+1 for k,v in enumerate(string.ascii_lowercase)}
num = [int(0.5*i*(i+1)) for i in range(1,30)]

f = open('C:/Users/Gray/Documents/Python Scripts/Project Euler/p042_words.txt')

for i in f:
    i = i.replace('"','')
    txt = i.split(',')

res = 0

for i in txt:
    count = 0
    for j in i:
        count += d[j.lower()]
    if count in num:
        res += 1

print(res)       
        
end = time.time()
print(end-start)