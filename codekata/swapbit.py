ipp1,ipp2=map(int,input().split())
ipp1=ipp1^ipp2
ipp2=ipp1^ipp2
ipp1=ipp1^ipp2
print(ipp1,ipp2)
