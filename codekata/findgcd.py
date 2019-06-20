def gcd(nu1,nu2):
  if(nu2==0):
    return nu1
  else:
    return gcd(nu2,nu1%nu2)
nu1,nu2=map(int,input().split())
print(gcd(nu1,nu2))
