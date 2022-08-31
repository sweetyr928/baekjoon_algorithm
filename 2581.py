m=int(input())
n=int(input())

sum=0;cnt=0;temp=n;

for i in range(m,n+1):
    if i==1:
        continue
    cnt=0
    for j in range(2,i):
        if i%j==0:
            cnt+=1
            break
    if cnt==0:
        if temp>i:
            temp=i
        sum+=i

if sum!=0:
    print(sum)
    print(temp)
else:
    print(-1)
