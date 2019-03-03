import time
start = time.time()

f = list(open('C:/Users/Gray/Documents/Python Scripts/Project Euler/p022_names.txt'))
a = f[0]
a = a.split('"')
b = []
for i in range(1,len(a)):
    if i%2 != 0:
        b.append(a[i].lower())
b = sorted(b)

name_value = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
score = 0
for pos,value in enumerate(b):
    count = 0
    for i in value:
        count += name_value[i]
    score += count*(pos+1)
    
print(score)

end = time.time()
print(end-start)