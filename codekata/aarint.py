def arm(st):
  a2=str(st)
  x=0
  for i in range(len(a2)):
    x=x+int(a2[i])**3
  if x == st:
    return True
  else:
    return False
  
a1=list(map(int,input().split()))
for i in range(a1[0]+1,a1[1]):
  if arm(i):
    print(i,end=' ')
