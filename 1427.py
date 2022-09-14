# import sys
# n = sys.stdin.readline()
# a = []
# for i in range(0,len(n)-1):
#     a.append(n[i])
# a.sort(reverse=True)
# for i in range (0,len(a)):
#     if i < len(a)-1:
#         print(a[i],end= '')
#     else:
#         print(a[i])

a = list(map(int, input()))
a.sort(reverse=True)

for i in a:
    print(i, end = '')
