import time
start = time.time()

p1_hands = []
p2_hands = []
f = open(r'C:\Users\Gray\Documents\Python Scripts\Project Euler\p054_poker.txt')
for i in f.readlines():
    p1_hands.append(i[:14])
    p2_hands.append(i[15:-1])

f.close()

card = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
suit = ['S','H','C','D']
rank = {'Royal Flush':10,'Straight FLush':9,'Four of a Kind':8,'Full House':7,'Flush':6,'Straight':5,'Three of a Kind':4,'Two Pair':3,'One Pair':2,'High Card':1}
d = {}

def high_card(n):
    p = []
    for i in card:
        if i in n:
            p.append(card[i])
    return p

def sets(n):
    d.clear()
    for i in card:
        if n.count(i) != 0:
            d[i] = n.count(i)
            if sum(d.values()) == 5:
                return d
    return d
    
def straight(n):
    st = []
    for i in n:
        if i in card:
            st.append(card[i])
    if len(set(st)) < 5:
        return False, 0
    st.sort()
    if st[0] == 2 and st[-1] == 14:
        st[-1] = 1
        st.sort()
    d = st[0] - st[1]
    i = 1
    while d == -1 and i < 4:
        d = st[i] - st[i+1]
        i += 1
    if d != -1:
        return False, 0
    return True, sum(st)

def flush(n):
    for i in suit:
        if n.count(i) == 5:
            return True
    return False

def value(n):
    st, st_sum = straight(n)
    fl = flush(n)
    if fl and st:
        if st_sum == 60:
            return [rank['Royal Flush']]
        else:
            return [rank['Straight Flush'], st_sum]
    se = sets(n)
    hc = high_card(n)
    if 4 in se.values():
        for k,v in se.items():
            if v == 4:
                return [rank['Four of a Kind'], card[k], hc[0] if hc[0] != card[k] else hc[1]]
    if 2 in se.values() and 3 in se.values():
        for k,v in se.items():
            if v == 3:
                return [rank['Full House'], card[k], hc[0] if hc[0] != card[k] else hc[1]] 
    if fl:
        return [rank['Flush'], hc[0], hc[1]]
    if st:
        return [rank['Straight'], st_sum]
    if 3 in se.values():
        for k,v in se.items():
            if v == 3:
                if hc[0] != card[k]:
                    return [rank['Three of a Kind'], k, hc[0], hc[1] if hc[1] != card[k] else hc[2]]
                else:
                    return [rank['Three of a Kind'], k, hc[1], hc[1]]
    if 2 in se.values():
        count, p = 0, []
        for k,v in se.items():
            if v == 2:
                count += 1
                p.append(card[k])
        if count == 2:
            if hc[0] != p[0]:
                if hc[0] != p[1]:
                    return [rank['Two Pair'], p[0], p[1], hc[0]]
                else:
                    return [rank['Two Pair'], p[0], p[1], hc[1] if hc[1] != p[0] else hc[2]]
            else:
                return [rank['Two Pair'], p[0], p[1], hc[1] if hc[1] != p[1] else hc[2]]
        else:
            if hc[0] != p[0]:
                if hc[1] != p[0]:
                    return [rank['One Pair'], p[0], hc[0], hc[1], hc[2] if hc[2] != p[0] else hc[3]]
                else:
                    return [rank['One Pair'], p[0], hc[0], hc[2], hc[3]]
            else:
                    return [rank['One Pair'], p[0], hc[1], hc[2], hc[3]]
    else:
        return [rank['High Card'], hc[0], hc[1], hc[2], hc[3], hc[4]]


def main():
    p1, p2 = 0, 0
    for i in range(len(p1_hands)):
        r1 = value(p1_hands[i])
        r2 = value(p2_hands[i])
        for j in range(6):
            if r1[j] != r2[j]:
                if r1[j] > r2[j]:
                    p1 += 1
                else:
                    p2 += 1
                break            
    return p1, p2
            
print(main())
       
end = time.time()
print(end-start)
