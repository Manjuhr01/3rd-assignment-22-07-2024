# WAP to count the number of vowels present in a string.
m=input("enter a string:")
vowels = 'aeiouAEIOU'
count = 0
index = 0

while index < len(m):
        if m[index] in vowels:
            count += 1
        index += 1
print(count)