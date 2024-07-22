#  WAP to count the number of occurrence of specified character.
# Ex: st = ‘pyspiders rajajinagara’
# ch = 'a'
# output = 5 (number of times 'a' is repeated)
# q=input("enter:")
# count = 0
# index = 0

# while index < len(q):
#         if q[index] == count:
#             count += 1
#         index += 1

# print(count)


st = 'pyspiders rajajinagara'
ch = 'a'

count = 0
index = 0

while index < len(st):
    if st[index] == ch:
        count += 1
    index += 1
print(count)
