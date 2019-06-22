    
lx, r = list(map(int,input().split()))

countk = 0

for i in range(1,101):

  if i*i >= lx and i*i <= r:

    countk += 1

print(countk)
