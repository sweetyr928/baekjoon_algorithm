all=int(input())
count = 0

while all >= 0:
  if all % 5 == 0:
    count += all // 5
    print(count)
    break

  all -= 3
  count += 1

else:
  print(-1)
