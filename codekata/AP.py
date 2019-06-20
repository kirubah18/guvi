A,B,Ci=map(int,input().split())
AP=0
for i in range(1,Ci+1):
 AP+=A+(Ci-i)*B
print(AP)
