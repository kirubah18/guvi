zy1,zy2=map(int,input().split())
mul=zy1*zy2
for k in range(0,mul+1):
  if(k**2==mul):
    print('yes')
    break
else:
  print('no')
