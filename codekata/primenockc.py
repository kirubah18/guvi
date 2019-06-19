py=int(input())
if (py>1):
  for i in range(2,py):
    if(py%i==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("yes")
