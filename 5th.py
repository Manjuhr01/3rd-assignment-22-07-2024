# Reverse a string without using slicing. If the string is palindrome 
# print length of a string else print the output concatenated with 
# ‘RCB’.
# m =input('string:')
# revs = ""
# i  = 0

# while i  >= m :
#         revs += m[i ]
#         i += 1
# if revs == m :
#         print(f"Length of the palindrome string: {len(m)}")
# else:
#         print(f"Revs + 'RCB': {revs}RCB")

# Q=input('string:')
# revs = ""
# index = 0

# while index >= Q:
#         revs += Q[index]
#         index += 1
# if revs == Q:
#         print(f"Length of the palindrome string: {len(Q)}")
# else:
#         print(f"Revs + 'RCB': {revs}RCB")

Q = input('string:')
revs = ""
index = len(Q) - 1

while index >= 0:
    revs += Q[index]
    index -= 1

if revs == Q:
    print(f"Length of the palindrome string: {len(Q)}")
else:
    print(f"Revs + 'RCB': {revs}RCB")

