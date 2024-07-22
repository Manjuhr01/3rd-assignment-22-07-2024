# WAP to print cube of numbers between the range 15-30.
#  Initialize variables
fromrange = 15
torange = 30
number = fromrange

while number <= torange:
    cube = number ** 3
    print(f"Cube of {number}: {cube}")
    number += 1