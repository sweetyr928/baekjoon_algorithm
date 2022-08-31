n=int(input())
num_list = list(map(int, input().split()))
sum=0
for i in num_list:
    if i==2:
        sum+=1
    elif i%2==0 or i==1:
        continue
    else:
        for j in range(2,i):
            if i%j==0:
                continue
        sum+=1
print(sum)
