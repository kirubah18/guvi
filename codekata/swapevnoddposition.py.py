stp=input()
for i in range(len(stp)):
  if (i%2==0):
    print(stp[i+1],end='')
  else:
    print(stp[i-1],end='')
