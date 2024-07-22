# WAP to replace space by ‘#’ of a string
# Ex: i/p → ‘ee sala cup namde’
# o/p → ‘ee#sala#cup#namde’
q=input("enter:")
index = 0
result = ""

while index < len(q):
        if q[index] == " ":
            result += "#"
        else:
            result += q[index]
        index += 1
print(result)