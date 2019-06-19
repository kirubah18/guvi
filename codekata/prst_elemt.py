x1,x2=map(int,input().split())
yi=list(map(int,input().split()))
count=0
if(len(yi)==x1):
 for i in yi:
  if(i==x2):
   count=1
 if(count==1):
  print('yes')
 else: 
  print('no')
