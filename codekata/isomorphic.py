si11, s2 = raw_input().split()
count = 0
for i in range(len(si11)):
  if si11.count(si11[i]) == s2.count(s2[i]):
    count += 1
if count == len(si11):
  print "yes"
else:
  print "no"
  
