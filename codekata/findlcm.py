def lcm(nu1,no2):
  if nu1>no2:
    a=nu1
  else:
    a=no2
  while(True):
    if a%nu1==0 and a%no2==0:
      l=a
      break
    a=a+1
  return l
  
nu1,no2=map(int,input().split())
ans=lcm(nu1,no2)
print(ans)
