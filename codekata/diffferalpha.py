mat2,jit2=map(str,input().split())

sayt2=0

if len(mat2)>len(jit2):

  mat2,jit2=jit2,mat2

i=0

while i<len(mat2):

  saty2+=(ord(jit2[i])-ord(mat2[i]))

  i+=1

for i in range(i,len(jit2)):

  saty2+=ord(jit2[i])-ord('a')+1

print(saty2)
