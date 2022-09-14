import sys
n = int(sys.stdin.readline())
a = []
for i in range (0,n):
    num1, num2 = map(int,input().split())
    a.append([num2,num1])
a.sort()
for i in range(0,len(a)):
    print(a[i][1],a[i][0])
