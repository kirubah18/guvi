sy=input()
c=0
d=0
for i in sy:
    if(i=='('):
        c=c+1
    if(i==')'):
        d=d+1
if(c==d):
    print("yes")
else:
    print("no")
