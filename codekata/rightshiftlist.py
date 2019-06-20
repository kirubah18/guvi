sy = [int(x) for x in input().split()]
sy1 = [int(x) for x in input().split()]
sy2=''
for i in range(0,sy[1]):
  sy1 = [sy1[-1]] + sy1[:-1]
print(*sy1,sep=' ')

#sy[:-1] returns the list by deleting the last element
