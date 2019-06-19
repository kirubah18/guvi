gy=input()
l=len(gy)
s=['a','e','i','o','u']
for i in range(0,l):
  if gy[i] in s:
    print("yes")
    break
else:
    print("no")
