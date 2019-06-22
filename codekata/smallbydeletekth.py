from itertools import combinations
ay1,b1=input().split()
a=str(ay1)
b=int(b1)
e=[]
d=combinations(a,len(a)-b)
for i in list(d):
    e.append("".join(i))
print(min(e))
