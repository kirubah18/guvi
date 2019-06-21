ky=int(input())
lk=list(map(int,input().split()))
c=[]
for i in lk:
    if(i==lk.index(i)):
        c.append(i)
print(*(sorted(c)))
if(len(c)==0):
    print(-1)
