so=int(input())
so1=input()
t=0
so2=['a','e','i','o','u']
for i in so1:
  if(i in so2):
    so1 = so1.replace(i,"")
print(so1[::-1])
