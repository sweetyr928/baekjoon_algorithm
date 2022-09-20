import sys
n = int(sys.stdin.readline())
a = []

for i in range (0,n):
    age, name = sys.stdin.readline().split()
    a.append([age,name])
a.sort(key=lambda x: int(x[0]))

for i in range(0,len(a)):
    print(a[i][0],a[i][1])
