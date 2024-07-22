
# wap to find some of all the odd num between the range of 20-60
m=20
k=60
sum= 0
for number in range(m, k + 1):
    if number % 2 != 0:
        sum += number
print(sum)