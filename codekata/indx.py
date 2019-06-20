ai=int(input())
ak=list(map(int,input().split()))
for i in ak:
    if ak[i]>ak[i+1]:
        print(i)
        break
