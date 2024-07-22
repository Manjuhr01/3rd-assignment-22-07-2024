# 15. WAP to find the greatest number in a given l of integers.
l = eval(input("enter:"))
i = 0
greatest_num=0
while i < len(l):
    if l[i] > greatest_num:
        greatest_num = l[i]
    i += 1

print(greatest_num)
