#  WAP to find the sum of cube of numbers in a given string.
string ='ab4hjk2dfjks12adsjk4'
out=145
q=input("enter a string:")
sum_of_cube = 0
current_number = ""
index = 0

while index < len(q):
        if q[index].isdigit():
            current_number += q[index]
            sum_of_cube += int(current_number) ** 3
        index += 1

print(sum_of_cube)
