# WAP to extract all the digits present in a string.
q=input("enter a string:")
index = 0
digits = []

while index < len(q):
        if q[index].isdigit():
            digits.append(int(q[index]))
        index += 1
print(digits)