nu1,nu2=input().split()
t=abs(len(nu1)-len(nu2))
for v in range(len(nu1)):
    if len(nu2)==1 and nu2[v] in nu1:
        break
    if nu1[v]!=nu2[v]:
        t+=1
print(t)
