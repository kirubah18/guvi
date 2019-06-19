ipi1=input()
dig=False
alpha=False
for i in ipi1:
  if(i.isdigit()):
    dig=True
  if(i.isalpha()):
    alpha=True
if(dig and alpha):
    print("Yes")
else:
    print("No")
