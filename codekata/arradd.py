a,b=input().split()
p=int(a)
q=int(b)
s=0
arr = [int(x) for x in input().split()]
for i in range (0,q):
  s=s+arr[i]
print(s)
