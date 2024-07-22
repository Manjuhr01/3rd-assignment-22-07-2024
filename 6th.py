# WAP to extract all the floating values of a tuple present at even 
# index and ends with even number and starts with odd number.
q=eval(input("tuple:"))
index = 0
result = []

while index < len(q):
        if index % 2 == 0:  
            current_value = q[index]
            if isinstance(current_value, float):
                result.append(current_value)
        index += 1
print(result)