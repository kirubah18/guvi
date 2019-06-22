s1x, s2, ki = list(map(str,input().split()))

ki = int(ki)

count = 0

for i in range(len(s1x)):

  if s1x[i] != s2[i]:

    count += 1

if count == ki:

  print("yes")

else:

  print("no")
