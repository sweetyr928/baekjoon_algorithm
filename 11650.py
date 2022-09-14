import sys
n = int(sys.stdin.readline())
a = []
for i in range (0,n):
    num = map(int,input().split())
    a.append(list(num))
a.sort()
for i in range(0,len(a)):
    print(a[i][0],a[i][1])
