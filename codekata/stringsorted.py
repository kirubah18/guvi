ly=[]
m=int(input())
a=input().split()
for i in a:
  ly.append(i)
ly.sort()
ly.sort(key=len)
for i in ly:
  print (i,end=' ')
