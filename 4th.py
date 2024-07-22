#  WAP to extract all the individual data items of a list. If length of 
# extracted output is more than 4, print the first value of output 
# else print last value of the output list and add 10 to it.
m = eval(input("enter a num list"))

i = 0
out = []

while i < len(m):
    out.append(m[i])
    i += 1

if len(out) > 4:
    print(f"First value: {out[0]}")
else:
    lv = out[-1] + 10
    print(f"Last_value + 10: {lv}")