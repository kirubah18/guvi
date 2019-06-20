ip=int(input())
rev22=0
while(ip>0):
  dig=ip%10
  rev22=rev22*10+dig
  ip=ip//10
print(rev22)
