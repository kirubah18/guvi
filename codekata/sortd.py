a=int(input())
ki=list(map(int,input().split()))
ki.sort()
for i in range(0,len(ki)):
  print(ki[i],end=' ')
