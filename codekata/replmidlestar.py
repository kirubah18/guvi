re=list(input())
l=len(re)
if(l%2==0):
  re[int(l/2)]='*'
  re[int((l/2)-1)]='*'
else:
  re[int(l//2)]='*'
for i in range(0,l):
  print(re[i],end='')
