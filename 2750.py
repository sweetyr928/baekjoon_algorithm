n = int(input())
a = []
for i in range (0,n):
    num = int(input())
    a.append(num)
a.sort()
for j in range (0,len(a)):
    print(a[j])
