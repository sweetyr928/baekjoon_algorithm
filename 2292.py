num=int(input())
temp = 1
piles = 1

while temp < num:
    temp = temp + (6 * piles)
    piles = piles + 1

print(piles)
