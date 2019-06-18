wordi=input()
itrq=0
for i in range (len(word)):
 if(wordi[i].isdigit() or wordi[i].isalpha() or wordi[i]==' '):
  continue
 else:
  itrq+=1
print(itrq) 
