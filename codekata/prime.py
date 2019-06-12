a1=input()
a=int(a1)
d=0
for e in range (2,a):
  c=a%e
  if(c==0):
    d=1+d
if(d!=0):
  print("no")
else:
  print("yes")
