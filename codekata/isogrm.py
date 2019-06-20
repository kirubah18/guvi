c11=input()
c2=""
for i in c11:
  if i not in c2:
    c2=c2+i
if(c11==c2):
  print("Yes")
else:
  print("No")
