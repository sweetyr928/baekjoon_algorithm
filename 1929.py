import math
m, n = map(int, input().split())
cnt=0
for i in range(m,n+1):
    if i==1:
        continue
    cnt=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            cnt+=1
            break
    if cnt==0:
        print(i)
