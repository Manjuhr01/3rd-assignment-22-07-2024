# Consider a list input, extract all the string inside it and print the
m=eval(input("input_list:"))
for i in m:
    if type(i) == str:
        print(i)

