x11,y11=input().split()
x11,y11=int(x11),int(y11)
x22,y22=input().split()
x22,y22=int(x22),int(y22)
x33,y33=input().split()
x33,y33=int(x33),int(y33)

if (y11 - y22) * (x11 - x33) == (y11 - y33) * (x11 - x22):
    print ("yes") 
else: 
    print ("no")
