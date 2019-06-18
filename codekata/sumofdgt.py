inpt=int(input())
sum=0
while(inpt>0):
 digit=inpt%10
 inpt=inpt//10
 sum+=digit
print(sum)
