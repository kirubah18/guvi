inpu1,inpu2=map(str,input().split())
list1=list(map(int,input().split()))
c=0
for i in list1:
    if i==int(inpu2):
        c=1
if c==1:    
     print("Yes")
else:
    print("No")
