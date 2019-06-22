lxy=[]

m=int(input())

a=input().split()

for i in a:

  lxy.append(i)

lxy.sort()

lxy.sort(key=len)

for i in lxy:

  print (i,end=' ')
