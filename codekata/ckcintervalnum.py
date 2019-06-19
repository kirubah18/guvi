o=int(input())
ki,l=input().split()
ki=int(ki)
l=int(l)
for i in range(ki,l):
  if(i==o):
   print("yes")
   break
else:
  print("no")
