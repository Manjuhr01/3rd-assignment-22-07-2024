# WAP to find sum of individual digits of a string.
# Ex: i/p = “im a 420 you are 840”
# o/p = 18





# k=input("enter a string including digits:")
# total = 0
# i = 0

# while i < len(k):
#        if 0<=k[i]<=9:
#             total += int(k[i])
#             i += 1
# print(total)


k=input("enter a string including digits:")
total = 0
i = 0

while i < len(k):
        if k[i].isdigit():
            total += int(k[i])
        i += 1
print(total)
