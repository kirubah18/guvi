ki=int(input())
ai=list(map(int,input().split()))
b=[]
for i in ai:
  if(ai.count(i)>1):
    b.append(i)
  else:
    print(i)
