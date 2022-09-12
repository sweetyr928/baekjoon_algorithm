import sys

n = int(input())

count = [0]*10001

for _ in range(n):
    x = int(sys.stdin.readline())
    count[x] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
