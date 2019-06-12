num = int(input())
s = 0
t = num
while t > 0:
   digit = t % 10
   s += digit ** 3
   t //= 10
if num == s:
   print("yes")
else:
   print ("no")
