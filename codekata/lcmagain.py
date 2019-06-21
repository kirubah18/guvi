xi,y=input().split()
xi,y=int(xi),int(y)
z=0
if xi > y:
  z = xi
else:
  z = y

while(True):
  if((z % xi == 0) and (z % y == 0)):
    lcm = z
    break
  z += 1
print(lcm)
