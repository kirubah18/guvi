sp=int(input())
s1=[(x) for x in input().split()]
for i in range(0,sp):
  if(s1.count(s1[i])==1):
    print(s1[i])
