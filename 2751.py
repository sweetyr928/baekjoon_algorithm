import sys
n = int(sys.stdin.readline())
a = []
for i in range (0,n):
    num = int(sys.stdin.readline())
    a.append(num)
a.sort()
for j in range (0,len(a)):
    print(a[j])
