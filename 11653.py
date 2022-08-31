n=int(input())
a=[]
while n>1:
    for i in range(2,n+1):
        cnt=0
        for j in range(2,i):
            if i%j==0:
                cnt+=1
                break
        if cnt==0:
            if n%i==0:
                a.append(i)
                n=n//i
for k in a:
    a.sort()
    print(k)
