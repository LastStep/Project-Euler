import time
start = time.time()

class words:
    def __init__(self):
        self.units = ['','one','two','three','four','five','six','seven','eight','nine'] 
        self.teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
        self.tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', 'eighty','ninety']
        self.hundred = 'hundred'
        self.thousand = 'thousand'

unit = words()

count = 0
for i in range(1,1001):
    if i<1000:
        rem = [int((i - i%100)/100), int((i%100 - i%10)/10), i%10]
        if i%100 < 20 and i%100 > 10:
            count += len(unit.teens[rem[2]])
            count -= len(unit.tens[rem[1]]) + len(unit.units[rem[2]])
        if i%100 == 0 or i < 100:
            count -= len('and')
            if i < 100:
                count -= len(unit.hundred)
        count += len(unit.units[rem[0]]) + len(unit.hundred) + len('and') + len(unit.tens[rem[1]]) + len(unit.units[rem[2]])
    else:
        rem = int(i/1000)
        count += len(unit.thousand) + len(unit.units[rem])
        
print(count)

end = time.time()
print(end-start)