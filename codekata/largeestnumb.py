a=int(input())
sys=list(map(int,input().split()))
yy=sorted(sys)[::-1]
z=""
if(sys==[0]*a):
    print("0")
else:
    for j in yy:
        z=z+str(j)
    print(int(z))
