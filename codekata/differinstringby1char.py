s11, s22 = input().split()
counts = 0
for i in range(len(s11)):
  if s11[i]!=s22[i]:
    counts=counts+1
if counts==1:
  print ("yes")
else:
  print ("no")
